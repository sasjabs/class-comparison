# Инструмент сравнения результатов классификации

Инструмент реализован в виде класса `Cross`
```python
class Cross()
```

# Основной метод
Выполнение сразу всего расчёта и экспорт результатов в файл
```python
Cross.Execute(rasters: list, output_gtiff: str, output_csv: str, sep: str = ',')
```
&ensp;&ensp;&ensp;&ensp;`rasters` - список файлов исходных категориальных растров в формате *GeoTiff* \
&ensp;&ensp;&ensp;&ensp;`output_gtiff` - выходной растровый файл в формате *GeoTiff* \
&ensp;&ensp;&ensp;&ensp;`output_csv` - выходная таблица в формате *.csv* \
&ensp;&ensp;&ensp;&ensp;`sep` - разделитель файла *.csv*. По умолчанию - запятая

## Другие методы
Выполняют логические шаги инструмента по отдельности 

\
Импорт растров
```python
Cross.ImportRasters(rasters: list)
```
&ensp;&ensp;&ensp;&ensp;`rasters` - список файлов (относительные пути) исходных категориальных растров в формате *GeoTiff*

\
Расчёт выходного растра
```python
Cross.CrossMap()
```
&ensp;&ensp;&ensp;&ensp;Выход: \
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`cross` - `numpy.array`, содержащий категориальные значения выходного растра \
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`reclass` - словарь, содержащий сопоставление новых классов комбинациям старых классов (в порядка импорта растров)

\
Экспорт файла стиля 
```python
Cross.ExportQML(output_qml: str)
```
&ensp;&ensp;&ensp;&ensp;`output_qml` - файл стиля слоя QGIS формата *.qml* для выходного растра, содержащий комбинации исходных классов в легенде

\
Экспорт итогового растра
```python
Cross.ExportMap(output_gtiff: str)
```
&ensp;&ensp;&ensp;&ensp;`output_geotiff` - выходной растровый файл в формате *GeoTiff*

\
Расчёт итоговой таблицы
```python
Cross.CrossTable()
```
&ensp;&ensp;&ensp;&ensp;Выход: `table` - словарь из списков, содержащий для каждого класса результирующего растра его код, комбинацию исходных классов, а также количество пикселей и их суммарную площадь

\
Экспорт итоговой таблицы
```python
Cross.ExportTable(output_csv: str, sep: str = ',')
```
&ensp;&ensp;&ensp;&ensp;`output_csv` - выходная таблица в формате *.csv* \
&ensp;&ensp;&ensp;&ensp;`sep` - разделитель файла *.csv*. По умолчанию - запятая

\
*Все файлы указываются в виде относительных путей*
