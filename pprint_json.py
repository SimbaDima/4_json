import json


def load_data_from_file(file_path):

    try:
        my_file = open(file_path, "r")
    except FileNotFoundError:
        return None
    data_load_from_file = json.load(my_file)
    my_file.close()
    return data_load_from_file


def pretty_print_json_in_console(data_load_from_file):
    print(json.dumps(data_load_from_file, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    data1 = load_data_from_file("C:\\Users\\User\\PycharmProjects\\firstTask\\jsonFormat.txt")
    pretty_print_json_in_console(data1)
