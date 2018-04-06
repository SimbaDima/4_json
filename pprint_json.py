import json


def load_data(filepath):

    try:
        myFile = open(filepath, "r")
    except FileNotFoundError:
        return None
    data = json.load(myFile)
    myFile.close()
    return data


def pretty_print_json(data):
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    data1 = load_data("C:\\Users\\User\\PycharmProjects\\firstTask\\jsonFormat.txt")
    pretty_print_json(data1)
