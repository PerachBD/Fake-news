import matplotlib.pyplot as plt
import csv
from process_data import data_features as DF

if __name__ == "__main__":
    data = []
    with open('../data/my_data.csv') as datafile:
        reader = [row for row in csv.DictReader(datafile)]
        for row in reader:
            source_url = row['source_url']
            date = row['date']
            title = row['title']
            authors = row['authors']
            images = row['images']
            fake_or_real = row['fake or real']
            obj = DF.DataFeatures(source_url, date, title, authors, images, fake_or_real, reader)
            data.append(obj)
    plt.plot(data)
    plt.show()
