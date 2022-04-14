from Cross import Cross

cr = Cross() # инициализация инструмента
rasters = ['data/Class1.tif', 'data/Class2.tif'] # исходные растры
outputRaster = 'output/CrossMap.tif' # путь к выходному растр
outputTable = 'output/CrossTable.csv' # путь к выходной таблице
cr.Execute(rasters, outputRaster, outputTable) # выполнение расчёта
