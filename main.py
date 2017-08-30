from collectors.fetch_data import news_from_url
from core import random_forest_model
from core.main_model import MainModel


def build_new_model():
    m = MainModel()
    m.build_model(model_list=[random_forest_model,])
    m.save_model()


def predict():
    m = MainModel()
    m.load_model()
    url = raw_input('Enter news url: ')
    print m.predict([news_from_url(url)])


if __name__ == '__main__':
    new_model = raw_input("Choose Option:\n------------\n1.Build New Model?\n2.Predict News\nPlease Enter Number\n")
    if new_model.lower() == '1':
        print 'start to build the model....'
        build_new_model()
    elif new_model.lower() == '2':
        predict()
    else:
        print 'Not Valid Input'
        exit(0)
