# Вывод данных из файла в консоль в формате JSON

Скрипт позволяет прочитать данные из файла (*данные в формате JSON*)(*скрипт запросит путь к файлу*), и вывести их в консоль тоже в формате JSON(*в удобном для чтения виде с отступами, переносами, пробелами*). 

# Как использовать

При помощи функции `loading_data_from_file(file_path)`, в аргументе которой лежит путь к файлу, мы выгружаем данные из файла в формате JSON, и копируем их в **data_from_file**
```python 
data_from_file = json.load(file_content_json)
return data_from_file
```
Эта функция возвратит **data_from_file** в которой находятся данные файла, если файл существует, в противном случае возвратится `None`  

Затем **data_from_file** подается на функцию `pretty_print_json_in_console(data_from_file)`, которая выводит данные в консоль в формате JSON.
```python
print(json.dumps(data_from_file, indent=4, sort_keys=True, ensure_ascii=False))
```
*indent=4* - отступы, *sort_keys=True* - включина сортировка по ключам, ensure_ascii=False - отключино  ascii.

**Пример использования**
Пользователя в консоли должен будет ввести путь к файлу
```python
print("enter path to file:")
file_path_user = input()
```    
Пусть пользователь ввел путь к файлу: C:\Users\User\PycharmProjects\firstTask\jsonFormat.txt. В jsonFormat.txt лежат данные в формате JSON: [{"name": "Dima", "level": "5"},{"name": "Ivan","level": "3"}]. 
```python 
data_file_user = loading_data_from_file(file_path_user)
pretty_print_json_in_console(data_file_user)
```
После выполнения скрипта, в консоль выведет данные тожу в формате JSON, только в удобном для чтения виде (с отступами, пробелами, сортировкой по ключам)


# Как запустить

Пример запуска скрипта на **Linux**, **Python 3.5**:

```bash

$ python pprint_json.py <path to file>
# TODO add output example

```

# Цели проекта 

Этот проект написан для образовательных целей. Обучающий курс для web-developers - [DEVMAN.org](https://devman.org)
