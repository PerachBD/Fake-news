import json
import os


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class Data(object):
    def __init__(self, data_file_path=os.path.abspath("data/my_data.json")):
        with open(data_file_path, 'r') as datafile:
            content = datafile.read()
            content = [] if content == '' else content
            self.data = json.loads(content)

    def get_data(self):
        return self.data
