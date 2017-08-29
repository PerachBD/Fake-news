from core import random_forest_model
from sklearn.externals import joblib
from newspaper import Article
from process_data.data_features import DataFeatures
import json
import os


def process_the_url(url):
    article = Article(url)
    article.download()
    article.html
    article.parse()
    strdate = str(article.publish_date)
    date = strdate.split(' ')
    if len(date) < 1:
        date.append('')
    test = [{'source_url': article.source_url, 'date': date[0], 'title': article.title, 'authors': article.authors,
         'images': article.images, 'text': article.text, 'fake or real': 'N'}]
    data_file_path = os.path.abspath("../data/my_data.json")
    data = []
    train_set = []
    with open(data_file_path, 'r') as datafile:
        content = datafile.read()
        content = [] if content == '' else content
        data = json.loads(content)
    DF = DataFeatures(test[0], data)
    return DF.get_features_list()

if __name__ == '__main__':
    new_model = raw_input("do u want to build a new model? (Y/N): ")
    clf = joblib.load('../data/saved_model.pkl')
    if new_model.lower() == 'y':
        random_forest_model.build_the_model()
    url = raw_input('enter news url: ')
    check = []
    check.append(process_the_url(url))
    preds = clf.predict(check)
    if preds == 1:
        print 'fake'
    else:
        print 'real'
