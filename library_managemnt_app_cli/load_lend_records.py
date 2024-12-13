import json

def load_lend_records():
    try:
        with open("lend_records.json", "r") as fp:
            lend_records = json.load(fp)
    except FileNotFoundError:
        lend_records = []
    return lend_records
