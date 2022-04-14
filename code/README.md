# Инструмент сравнения результатов классификации

Инструмент реализован в виде класса `Cross`
```python
class Cross(wdir = None)
```
&ensp;&ensp;&ensp;&ensp;`wdir` - рабочая директория инструмента, задаётся при инициализации экземпляра класса

# Основной метод:
`Cross.Execute` - выполнение сразу всего расчёта и экспорт результатов в файл
```python
Cross.Execute(rasters: list, output_gtiff: str, output_csv: str, sep: str = ',')
```
&ensp;&ensp;&ensp;&ensp;`rasters` - список файлов исходных категориальных растров в формате GeoTiff \
&ensp;&ensp;&ensp;&ensp;`output_gtiff` - выходной растровый файл в формате GeoTiff \
&ensp;&ensp;&ensp;&ensp;`output_csv` - выходная таблица в формате *.csv* \
&ensp;&ensp;&ensp;&ensp;`sep` - разделитель файла *.csv*. По умолчанию - запятая

## Другие методы
Выполняют логические шаги инструмента по отдельности 

`Cross.ImportRasters` - импорт растров
```python
Cross.ImportRasters(rasters: list)
```
&ensp;&ensp;&ensp;&ensp;`rasters` - список файлов (относительные пути) исходных категориальных растров в формате GeoTiff 

\
`Cross.CrossMap` - расчёт выходного растра

```python
Cross.CrossMap()
```
&ensp;&ensp;&ensp;&ensp;Выход: \
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`cross` - `numpy.array`, содержащий категориальные значения выходного растра \
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;`reclass` - словарь, содержащий сопоставление новых классов комбинациям старых классов (в порядка импорта растров)


*Все файлы указываются в виде относительных путей*
