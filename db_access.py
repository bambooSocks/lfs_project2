import json


def loadDB():
    f = open("db.json")
    data = json.load(f)
    f.close()
    return data
