from process_data import get_image_info
import enchant
from zlib import crc32


class News(object):
    FAKE = 'Fake'
    REAL = 'Real'

    def __init__(self, params, all_dataset):
        # source_url, date, title, authors, images, text, fake_or_real, all_dataset
        self.title_large_letters_and_exclamation_points = News.title_large_letters_and_exclamation_points(params.get('title', ''))
        self.year_of_news = News.year_of_news(params.get('date', None))
        self.month_of_news = News.month_of_news(params.get('date', None))
        self.day_of_news = News.day_of_news(params.get('date', None))
        self.source_url = params.get('source_url', '')
        self.number_of_webs_that_publish_this_title = News.number_of_webs_that_publish_this_title(params.get('title', ''), params.get('source_url', ''), all_dataset)
        self.authors = params.get('authors', '')
        self.authors_record = News.authors_record(params.get('source_url', ''), params.get('authors', ''), all_dataset)
        # self.if_web_familiar = DataFeatures.if_web_familiar(source_url)
        self.counter_spelling_mistakes = News.counter_spelling_mistakes(params.get('title', ''), params.get('text', ''))
        self.search_images_gps_source = News.gps_images_source(params.get('images', ''))
        # self.check_contact_info = News.check_contact_info()
        # self.strange_or_similar_to_large_site = News.strange_or_similar_to_large_site()
        # self.check_if_title_extreme_or_not_related_to_text = News.check_if_title_extreme_or_not_related_to_text()
        self.fake_or_real = params.get('fake or real', '')

    @classmethod
    def title_large_letters_and_exclamation_points(cls, title):
        if any(x.isupper() for x in title):
            return True
        if '!' in title:
            return True
        return False

    @classmethod
    def check_if_relevant_date(cls, str_date):
        date = str_date.split('-')
        return date

    @classmethod
    def year_of_news(cls, str_date):
        date = str_date.split('-')
        return date[0] if date[0] != 'None' else None

    @classmethod
    def month_of_news(cls, str_date):
        date = str_date.split('-')
        if len(date)>1:
            return date[1]

    @classmethod
    def day_of_news(cls, str_date):
        date = str_date.split('-')
        if len(date) > 2:
            return date[2]

    @classmethod
    def number_of_webs_that_publish_this_title(cls, title, source_url, reader):
        count = 0
        for row in reader:
            if row['title'] == title and row['source_url'] != source_url:
                count = count + 1
        return count

    @classmethod
    def authors_record(cls, source_url, author, reader):
        """
        Count the number of times that the authors publish real news
        """
        count = 0
        for row in reader:
            if row['authors'] == author and row['source_url'] != source_url and row['fake or real'] == 'R':
                count = count + 1
        return count

    @classmethod
    def counter_spelling_mistakes(cls, title, text):
        counter = 0
        d = enchant.Dict("en_US")
        for x in title:
            if not d.check(x):
                counter = counter + 1
        for x in text:
            if not d.check(x):
                counter = counter + 1
        return counter

    @classmethod
    def gps_images_source(cls, images):
        lat, lon = [], []
        for image in images:
            exif_data = get_image_info.get_exif_data(image)
            x, y = get_image_info.get_lat_lon(exif_data)
            lat.append(x)
            lon.append(y)
        return lat, lon

    @classmethod
    def if_web_familiar(cls, source_url):
        raise NotImplemented

    @classmethod
    def check_contact_info(cls):
        raise NotImplemented

    @classmethod
    def strange_or_similar_to_large_site(cls):
        raise NotImplemented

    @classmethod
    def check_if_title_extreme_or_not_related_to_text(cls):
        raise NotImplemented

    def get_features_list(self):
        features = list()
        features.append(1 if self.title_large_letters_and_exclamation_points else 0)
        features.append(float(self.year_of_news if self.year_of_news is not None else 0))
        features.append(float(self.month_of_news if self.month_of_news is not None else 0))
        features.append(float(self.day_of_news if self.day_of_news is not None else 0))
        features.append(self.number_of_webs_that_publish_this_title)
        features.append(self.authors_record)
        features.append(self.counter_spelling_mistakes)
        features.append(str_to_float(self.source_url))
        features.append(str_to_float(self.authors[0]) if len(self.authors) >= 1 else 0)
        # features.append(str_to_float(self.search_images_gps_source))
        # features.append(self.check_contact_info)
        # features.append(self.strange_or_similar_to_large_site)
        # features.append(self.check_if_title_extreme_or_not_related_to_text)
        return features

    def get_label(self):
        return 1 if self.fake_or_real.lower() == 'F'.lower() else 0


def bytes_to_float(b):
    return float(crc32(b) & 0xffffffff)


def str_to_float(s, encoding="utf-8"):
    return bytes_to_float(s.encode(encoding))
