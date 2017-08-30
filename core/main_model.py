from sklearn.externals import joblib
from models.news import News


def ask_expert():
    while True:
        answer = raw_input('Expert need to help [F/R]?')
        if answer == 'F':
            return News.FAKE
        if answer == 'R':
            return News.REAL


class MainModel(object):
    def __init__(self):
        self.models = []

    def build_model(self, model_list):
        for model in model_list:
            self.models.append(model.build_model())

    def predict(self, news):
        fake_counter = 0
        for module in self.models:
            fake_counter += module.predict(news)
        tot_pred = (float(fake_counter) / len(self.models))
        if tot_pred > 0.5:
            return News.FAKE
        elif tot_pred == 0.5:
            return ask_expert()
        else:
            return News.REAL

    def save_model(self, out_file='data/saved_model.pkl'):
        joblib.dump(self.models, out_file)

    def load_model(self, in_file='data/saved_model.pkl'):
        self.models = joblib.load(in_file)
