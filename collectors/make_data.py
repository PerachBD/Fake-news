from newspaper import Article
import json
import os

fake_or_real = raw_input("enter F for fake and R for real: ")
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

# with open("../data/my_data.json", "a+") as datafile:
#     datafile.write(dumps({'source_url': article.source_url, 'date': date[0], 'title': article.title, 'authors': article.authors, 'images': article.images, 'text': article.text, 'fake or real': fake_or_real}, datafile, indent=7))
# datafile.close()
#

data_file_path = os.path.abspath("../data/my_data.json")
data = []
with open(data_file_path, 'r+') as datafile:
    content = datafile.read()
    content = [] if content == '' else content
    data = json.loads(content)
    data.append({'source_url': article.source_url, 'date': date[0], 'title': article.title, 'authors': article.authors,
         'images': article.images, 'text': article.text, 'fake or real': fake_or_real})

with open(data_file_path, 'w') as datafile:
    datafile.write(json.dumps(data))