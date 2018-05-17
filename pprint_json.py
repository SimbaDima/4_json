import json
import sys


def load_data_from_file(file_path_of_user):
    try:
        with open(file_path_of_user) as object_of_file:
                data_from_file = json.load(object_of_file)
        return data_from_file
    except json.decoder.JSONDecodeError:
        return None


def pretty_print_json(data_from_file):
    print(json.dumps(data_from_file, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    try:
        data_file_user = load_data_from_file(sys.argv[1])
        pretty_print_json(data_file_user)
    except FileNotFoundError:
        print("file does not exist with that name")
    except TypeError:
        print("missing required parameter in function <load_data_from_file>")
    except IndexError:
        print("after name of script will be file c data in format json ")


