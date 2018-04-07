# Вывод данных из файла в консоль в формате JSON

Скрипт позволяет прочитать данные из файла (*данные в формате JSON*)(*скрипт запросит путь к файлу*), и вывести их в консоль тоже в формате JSON(*в удобном для чтения виде с отступами, переносами, пробелами*). 

# Как использовать

При помощи функции `load_data_from_file(filepath)`, в аргументе которой лежит путь к файлу, мы выгружаем данные из файла в формате JSON, и копируем их в **data_load_from_file**
```python 
data_load_from_file = json.load(my_file)
return data_load_from_file
```
Эта функция возвратит **data_load_from_file** в которой находятся данные файла.

Затем **data_load_from_file** подается на функцию pretty_print_json_in_console(data_load_from_file), которая выводит данные в консоль в формате JSON.
```
print(json.dumps(data_load_from_file, indent=4, sort_keys=True, ensure_ascii=False))
```
*indent=4* - отступы, *sort_keys=True* - включина сортировка по ключам, ensure_ascii=False - отключино  ascii.

**Пример использования**
```
data1 = load_data_from_file("C:\\Users\\User\\PycharmProjects\\firstTask\\jsonFormat.txt")
pretty_print_json_in_console(data1)
```

# Как запустить

Пример запуска скрипта на **Linux**, **Python 3.5**:

```bash

$ python pprint_json.py <path to file>
# TODO add output example

```

# Цели проекта 

Этот проект написан для образовательных целей. Обучающий курс для web-developers - [DEVMAN.org](https://devman.org)
