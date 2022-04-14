<qgis hasScaleBasedVisibilityFlag="0" maxScale="0" minScale="1e+08" styleCategories="AllStyleCategories" version="3.14.15-Pi">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <temporal enabled="0" fetchMode="0" mode="0">
    <fixedRange>
      <start />
      <end />
    </fixedRange>
  </temporal>
  <customproperties>
    <property key="WMSBackgroundLayer" value="false" />
    <property key="WMSPublishDataSourceUrl" value="false" />
    <property key="embeddedWidgets/count" value="0" />
    <property key="identify/format" value="Value" />
  </customproperties>
  <pipe>
    <rasterrenderer alphaBand="-1" band="1" nodataColor="" opacity="1" type="paletted">
      <rasterTransparency />
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <colorPalette>
      <paletteEntry alpha="255" color="#1e6cdd" label="1-1" value="1" /><paletteEntry alpha="255" color="#f7c391" label="1-2" value="2" /><paletteEntry alpha="255" color="#7023c8" label="2-1" value="3" /><paletteEntry alpha="255" color="#eb1e5f" label="2-2" value="4" /></colorPalette>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0" />
    <huesaturation colorizeBlue="128" colorizeGreen="128" colorizeOn="0" colorizeRed="255" colorizeStrength="100" grayscaleMode="0" saturation="0" />
    <rasterresampler maxOversampling="2" />
  </pipe>
  <blendMode>0</blendMode>
</qgis>