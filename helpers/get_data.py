import csv
import json


def get_data_from_csv(file: str):
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for el in reader:
            yield el


def get_data_from_json(file: str):
    with open('../files/file.json', "r") as f:
        users = json.load(f)

    return users['users']



def id_val(val):
    return val[0]