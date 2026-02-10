import json, os

def load_data():
    with open(os.path.join('data_manager', 'data.json')) as file:
        data = json.load(file)
    return data
