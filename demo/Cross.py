import numpy as np
import random
from osgeo import gdal, gdalconst, gdal_array
import xml.etree.ElementTree as ET
import os
from itertools import product


class Cross:
    def __init__(self):
        self.grd_params = None
        self.arrays = None
        self.cross = None
        self.reclass = None
        self.nodata = None
        return

    def ImportRasters(self, rasters: list):
        self.num_rasters = len(rasters)

        datasets = []
        projs = []
        lefts = []
        rights = []
        tops = []
        bottoms = []

        # определение параметров сетки, к которой будут приведены все растры
        for raster in rasters:
            ds = gdal.Open(raster)
            if ds is None:
                raise ValueError(f'Файл {raster} не найден')
            self.nodata = ds.GetRasterBand(1).GetNoDataValue()
            datasets.append(ds)

            proj = ds.GetProjection()
            projs.append(proj)

            gtf = ds.GetGeoTransform()
            left, top, xcs, ycs = gtf[0], gtf[3], gtf[1], gtf[5]
            width, height = ds.RasterXSize, ds.RasterYSize
            right = left + width * xcs
            bottom = top + height * ycs
            lefts.append(left)
            rights.append(right)
            tops.append(top)
            bottoms.append(bottom)

        if len(set(projs)) != 1:
            raise ValueError('Координатные системы растров не совпадают')

        ref_gtf = datasets[0].GetGeoTransform()
        ref_xcs, ref_ycs = ref_gtf[1], ref_gtf[5]

        xmin, xmax, ymin, ymax = min(lefts), max(rights), min(bottoms), max(tops)
        grd_gtf = (xmin, ref_xcs, ref_gtf[2], ymax, ref_gtf[4], ref_ycs)
        grd_proj = projs[0]
        grd_width = int((xmax - xmin) // ref_xcs)
        grd_height = int((ymin - ymax) // ref_ycs)

        self.grd_params = {'gtf': grd_gtf, 'proj': grd_proj,
                           'width': grd_width, 'height': grd_height}
        self.arrays = []

        # приведение всех растров к одной сетке
        for ds in datasets:
            dst = gdal.GetDriverByName('GTiff').Create('_temp.tif', grd_width, grd_height, 1, gdalconst.GDT_UInt32)
            dst.GetRasterBand(1).SetNoDataValue(self.nodata)
            dst.SetGeoTransform(grd_gtf)
            dst.SetProjection(grd_proj)

            gdal.ReprojectImage(ds, dst, grd_proj, grd_proj, gdalconst.GRA_NearestNeighbour)
            del dst

            al_arr = gdal_array.LoadFile('_temp.tif')
            self.arrays.append(al_arr)
            del al_arr
            gdal.Unlink('_temp.tif')

        self.arrays = np.array(self.arrays)

        values = [np.unique(arr) for arr in self.arrays]
        perm = list(product(*values))
        perm = [p for p in perm if self.nodata not in p]
        classes = [i + 1 for i in range(len(perm))]

        self.reclass_match = dict(zip(perm, classes))
        self.reverse_match = dict(zip(classes, perm))

    def ReclassComb(self, comb):
        if self.nodata not in comb:
            return self.reclass_match[tuple(comb)]
        else:
            return self.nodata

    def CrossMap(self):
        cross = np.apply_along_axis(self.ReclassComb, 0, self.arrays)

        classes = np.unique(cross)
        reclass = {k: v for k, v in self.reverse_match.items() if k in classes}

        self.cross = cross
        self.reclass = reclass

        return cross, reclass

    def ExportQML(self, output_qml):
        tree = ET.parse('qml_template.qml')
        cp = tree.find(".//colorPalette")
        r = lambda: random.randint(0, 255)
        for k, values in self.reclass.items():
            label = '-'.join([str(v) for v in values])
            color = '#%02x%02x%02x' % (r(), r(), r())
            ET.SubElement(cp, "paletteEntry",
                          attrib={"value": str(k),
                                  "alpha": "255",
                                  "label": label,
                                  "color": color})

        tree.write(output_qml)

    def ExportMap(self, output_gtiff):
        output = gdal.GetDriverByName('GTiff').Create(output_gtiff, self.grd_params['width'],
                                                      self.grd_params['height'], 1, gdalconst.GDT_UInt32)
        output.SetGeoTransform(self.grd_params['gtf'])
        output.SetProjection(self.grd_params['proj'])

        output.GetRasterBand(1).WriteArray(self.cross)
        output.GetRasterBand(1).SetNoDataValue(self.nodata)
        output.FlushCache()

        del output

    def CrossTable(self):
        if self.cross is None:
            self.CrossMap()

        class_columns = [f'Class{i + 1}' for i in range(self.num_rasters)]
        columns = ['NewClass'] + class_columns + ['PixCount', 'Area']

        classes, count = np.unique(self.cross, return_counts=True)
        count = count[classes != self.nodata]
        classes = classes[classes != self.nodata].astype(np.int32)

        cell_area = np.abs(self.grd_params['gtf'][1] * self.grd_params['gtf'][5])
        areas = (cell_area * count).astype(np.float64)
        class_lists = [[self.reclass[c][i] for c in classes] for i in range(self.num_rasters)]

        data = [list(classes), *class_lists, list(count), list(areas)]
        table = dict(zip(columns, data))
        self.table = table
        return table

    def ExportTable(self, output_csv, sep: str = ','):
        tbl = self.table
        data = list(tbl.values())
        header = sep.join(tbl.keys()) + '\n'

        with open(output_csv, 'w') as out:
            out.write(header)
            for i, _ in enumerate(tbl['NewClass']):
                line_lst = [str(lst[i]) for lst in data]
                line = sep.join(line_lst) + '\n'
                out.write(line)

    def Execute(self, rasters: list, output_gtiff: str, output_csv: str, sep: str = ','):
        self.ImportRasters(rasters)
        self.CrossTable()
        self.ExportMap(output_gtiff)
        self.ExportQML(os.path.splitext(output_gtiff)[0] + '.qml')
        self.ExportTable(output_csv, sep)