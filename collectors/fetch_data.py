from newspaper import Article
from models.data_set import Data
from models.news import News


def news_from_url(url):
    article = Article(url)
    article.download()
    article.html
    article.parse()
    str_date = str(article.publish_date)
    date = str_date.split(' ')
    if len(date) < 1:
        date.append('')
    test = {'source_url': article.source_url,
            'date': date[0],
            'title': article.title,
            'authors': article.authors,
            'images': article.images,
            'text': article.text,
            'fake or real': 'N'}
    data = Data().get_data()
    return News(test, data).get_features_list()
