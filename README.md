# class-comparison
Инструмент, повторяющий функциональность инструмента [Cross](http://spatial-analyst.net/ILWIS/htm/ilwisapp/cross_functionality.htm) из пакета ILWIS - сравнение результатов классификации изображений \
Инструмент можно запускать в любой среде Python, в том числе встроенной в QGIS (Консоль Python)

Входными данными для инструмента является произвольное количество (минимум 2) категориальных растров классификации. \
Выходом является растр, содержащий отдельный класс на каждую уникальную комбинацию исходных категорий, а также таблица, в которой для каждой комбинации записано количество пикселей и их суммарная площадь

Python tool replicating ILWIS Cross tool for comparing image classification results \
Possible to use from any common Python IDE or built-in QGIS IDE

