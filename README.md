# Outputting data from a file to the console in JSON format

The script allows you to read data from a file (*data in the **JSON** format*) (*the script will ask for the path to the file*), and print them to the console in the format **JSON** (*in an easy-to-read form with indents, hyphenation, spaces*).

# How to use

Using the `load_data_from_file (file_path)` function, whose argument is the path to the file, we upload the data from the file in **JSON** format, and copy them to `data_from_file`
```python

data_from_file = json.load (file_content_json)
return data_from_file

```
This function will return `data_from_file` in which the file data is located, if the file exists, otherwise `None`

Then `data_from_file` is supplied to the function `pretty_print_json_in_console (data_from_file)`, which prints data to the console in **JSON** format.
```python

print (json.dumps (data_from_file, indent = 4, sort_keys = True, ensure_ascii = False))

```

**Example of use**
The user in the console must enter the path to the file
```python

print ("enter path to file:")
file_path_user = input ()

```
Let the user enter the path to the file: *C: \ Users \ User \ PycharmProjects \ firstTask \ jsonFormat.txt*. The file *jsonFormat.txt* contains data in the format **JSON**: *[{"name": "Dima", "level": "5"}, {"name": "Ivan", "level": "3"}]*.

```python

data_file_user = loading_data_from_file (file_path_user)
pretty_print_json_in_console (data_file_user)

```
After executing the script, the console will display the data in the **JSON** format, only in an easy-to-read form (with indentations, spaces, sorting by keys)


# How to start

Example of running the script on **Linux**, **Python 3.5**:

```bash

$ python pprint_json.py <path to file>
# TODO add output example

```

# Project Objectives

This project is written for educational purposes. Training course for web-developers - [DEVMAN.org] (https://devman.org)
