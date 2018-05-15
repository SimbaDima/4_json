# Outputting data from a file to the console in JSON format

The script allows you to read data from a file (*data in the **JSON** format*), and print them to the console in the format **JSON** (*in an easy-to-read form with indents, hyphenation, spaces*).

# How to use

Using the `loading_data_from_file(file_path_of_user)` function, whose argument is the path to the file, we upload the data from the file in **JSON** format, and copy them to `data_of_file`
```python

data_of_file = json.load(object_of_file)
return data_of_file

```
This function will return `data_of_file` in which the file data is located, if the file exists, otherwise `None`

Then `data_of_file` is supplied to the function `pretty_print_json (data_of_file)`, which prints data to the console in **JSON** format.
```python

print (json.dumps (data_from_file, indent = 4, sort_keys = True, ensure_ascii = False))

```
In the following lines

```python

data_file_user = loading_data_from_file(sys.argv[1])
pretty_print_json(data_file_user)

```
we use our functions, `sys.argv[1]` - with these argument, we pass the file name through the console.


# How to start

Example of running the script on **cmd of Windows**, **Python 3.5**:

```bash

> python pprint_json.py <name of file>

```

# Example of use

The console allows you to use autocompletion, which is very convenient, to start we need to go to the directory where our script and the data file are located, then look at the point how to start and spell this into the console

```bash

>cd C:/Users/User/PycharmProjects/firstTask
> python pprint_json.py dataJson.txt

```
The dataJson.txt file contains data: *[{"name": "Dima", "level": "5"},{"name": "Ivan","level": "3"}]*
After you run the script, you will see

{
        "level": "5",
        "name": "Dima"
    },
    {
        "level": "3",
        "name": "Ivan"
 }
 
# Project Objectives

This project is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
