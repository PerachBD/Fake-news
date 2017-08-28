from newspaper import Article
from json import dumps, load

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
# print article.text

strdate = str(article.publish_date)
date = strdate.split(' ')

with open("../data/my_data.txt", "a+") as datafile:
    datafile.write(dumps({'source_url': article.source_url, 'date': date[0], 'title': article.title, 'authors': article.authors, 'images': article.images, 'text': article.text, 'fake or real': fake_or_real}, datafile, indent=7))
datafile.close()

with open("../data/my_data.txt", "r") as s:
    print(s.read())
