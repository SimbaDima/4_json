import json


def loading_data_from_file(file_path):
    try:
        with open(file_path) as file_content_json:
            data_from_file = json.load(file_content_json)
    except FileNotFoundError:
        return None

    return data_from_file


def pretty_print_json_in_console(data_from_file):
    print(json.dumps(data_from_file, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    print("enter path to file:")
    file_path_user = input()
    data_file_user = loading_data_from_file(file_path_user)
    pretty_print_json_in_console(data_file_user)
