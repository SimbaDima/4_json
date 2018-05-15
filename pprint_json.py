import json
import sys


def loading_data_from_file(file_path_of_user):
    try:
        with open(file_path_of_user) as object_of_file:
            data_of_file = json.load(object_of_file)
        return data_of_file
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        return None
#не знаю как обработать исключение, когда нет параметров в функции

def pretty_print_json(data_of_file):
    print(json.dumps(data_of_file, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    data_file_user = loading_data_from_file("tx.txt")
    pretty_print_json(data_file_user)
