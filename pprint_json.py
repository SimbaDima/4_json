import json


def loading_data_from_file(file_path_of_user):
    try:
        with open(file_path_of_user) as object_of_file:
            data_format_json = json.load(object_of_file)
    except FileNotFoundError:
        return None

    return data_format_json


def pretty_print_json(data_format_json):
    print(json.dumps(data_format_json, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    print("enter path to file:")
    file_path_user = input()
    data_file_user = loading_data_from_file(file_path_user)
    pretty_print_json(data_file_user)
