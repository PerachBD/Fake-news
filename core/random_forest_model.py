from sklearn.ensemble import RandomForestClassifier
from clssification import get_dataset
import random
from sklearn.externals import joblib


def separate_trainset_and_testset():
    allset = get_dataset()
    random.shuffle(allset)
    index_split = int(len(allset) * 0.7)
    train_data = allset[:index_split]
    test_data = allset[index_split:]
    return train_data, test_data


def fit_set_to_model(data):
    X, Y = [], []
    for row in data:
        Y.append(row.get_label())
        X.append(row.get_features_list())
    return X, Y


def Accuracy(TruePositive, FalseNegative, FalsePositive, TrueNegative):
    return (float(TruePositive + TrueNegative) / (TruePositive + TrueNegative + FalsePositive + FalseNegative)) * 100

# def Precision(TruePositive, FalseNegative, FalsePositive, TrueNegative):


def build_the_model():
    def make_test(testset):
        count = 0
        TruePositive, FalseNegative, FalsePositive, TrueNegative = 0, 0, 0, 0
        x, y = fit_set_to_model(testset)
        result = clf.predict(x)
        for row in range(0, len(testset)):
            if result[row] and y[row]:
                TruePositive = TruePositive + 1
            elif not result[row] and y[row]:
                FalseNegative = FalseNegative + 1
            elif result[row] and not y[row]:
                FalsePositive = FalsePositive + 1
            else:
                TrueNegative = TrueNegative + 1
        return TruePositive, FalseNegative, FalsePositive, TrueNegative
    train, test = separate_trainset_and_testset()
    X, Y = fit_set_to_model(train)
    clf = RandomForestClassifier(max_depth=4, random_state=0)
    model = clf.fit(X, Y)
    print(clf.feature_importances_)
    TP, FN, FP, TN = make_test(test)
    print 'TruePositive: ', TP, ' FalseNegative: ', FN, ' FalsePositive: ', FP, ' TrueNegative: ', TN
    print 'Accuracy: ', Accuracy(TP, FN, FP, TN)
    joblib.dump(clf, '../data/saved_model.pkl')


if __name__ == '__main__':
    build_the_model()