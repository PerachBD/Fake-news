from models.data_set import Data
from models.news import News


def get_data_set():
    train_set = []
    data = Data().get_data()
    for x in data:
        train_set.append(News(x, data))
    return train_set

