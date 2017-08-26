from newspaper import Article
import csv

fake_or_real = raw_input("entr F for fake and R for real: ")
url = raw_input('enter news url: ')
article = Article(url)

article.download()
article.html
article.parse()

# print article.title
# print article.authors
# print article.source_url
# print article.movies
# print article.publish_date

datafile = '../data/my_data.csv' if fake_or_real == 'R' else '../data/fake_data.csv'
headers = ['source_url', 'date', 'title', 'authors', 'images', 'fake or real']
fields = [article.source_url, article.publish_date, article.title, article.authors, article.images, fake_or_real]


with open(datafile, 'a') as f:
    writer = csv.writer(f)
    # writer.writerow(headers)
    writer.writerow(fields)


with open(datafile) as s:
    print(s.read())
