import os

wdir = 'C:/Users/kcher/Desktop/sem10/space/cross_demo'
os.chdir(wdir) # установка рабочей директории

from Cross import Cross # импорт инструмента из Cross.py

cr = Cross() # инициализация инструмента

rasters = ['data/Class1.tif', 'data/Class2.tif'] # список входных растров
outputRaster = 'output/CrossMap.tif' # путь к выходному растру
outputTable = 'output/CrossTable.csv' # путь к выходной таблице
cr.Execute(rasters, outputRaster, outputTable) # выполнение расчёта

# добавление таблицы и выходного растра на интерфейс
tbl_uri = f"file:///{wdir}/{outputTable}?delimiter=,"
iface.addVectorLayer(tbl_uri, "Cross Table", "delimitedtext")
iface.addRasterLayer(outputRaster, "Cross Map")