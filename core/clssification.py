import matplotlib.pyplot as plt
import json
from process_data import data_features as DF
import os


def get_dataset():
    data_file_path = os.path.abspath("../data/my_data.json")
    data = []
    train_set = []
    with open(data_file_path, 'r+') as datafile:
        content = datafile.read()
        content = [] if content == '' else content
        data = json.loads(content)
        for x in data:
            train_set.append(DF.DataFeatures(x, data))
    return train_set

