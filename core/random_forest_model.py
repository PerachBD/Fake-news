from sklearn.ensemble import RandomForestClassifier
from clssification import get_data_set
import random


def separate_train_and_test_set(train_size=0.7):
    all_set = get_data_set()
    random.shuffle(all_set)
    index_split = int(len(all_set) * train_size)
    train_data = all_set[:index_split]
    test_data = all_set[index_split:]
    return train_data, test_data


def fit_set_to_model(data):
    X, Y = [], []
    for row in data:
        Y.append(row.get_label())
        X.append(row.get_features_list())
    return X, Y


def accuracy(true_positive, false_negative, false_positive, true_negative):
    return (float(true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative)) * 100


def build_model():
    def make_test(test_set):
        true_positive, false_negative, false_positive, true_negative = 0, 0, 0, 0
        x, y = fit_set_to_model(test_set)
        result = clf.predict(x)
        for row in range(0, len(test_set)):
            if result[row] and y[row]:
                true_positive += 1
            elif not result[row] and y[row]:
                false_negative += 1
            elif result[row] and not y[row]:
                false_positive += 1
            else:
                true_negative += 1
        return true_positive, false_negative, false_positive, true_negative
    train, test = separate_train_and_test_set()
    X, Y = fit_set_to_model(train)
    clf = RandomForestClassifier(max_depth=4, random_state=0)
    model = clf.fit(X, Y)
    tp, fn, fp, tn = make_test(test)
    print 'TruePositive: ', tp, ' FalseNegative: ', fn, ' FalsePositive: ', fp, ' TrueNegative: ', tn
    print 'accuracy: ', accuracy(tp, fn, fp, tn)
    return model
