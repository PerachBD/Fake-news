import csv
# from iptcinfo import IPTCInfo
from process_data import get_image_info
import enchant
from zlib import crc32
d = enchant.Dict("en_US")


class DataFeatures:

    @classmethod
    def title_large_letters_and_exclamation_points(cls, title):
        if any(x.isupper() for x in title):
            return True
        if '!' in title:
            return True
        return False

    @classmethod
    def CheckIfRelevantDate(cls, strdate):
        date = strdate.split('-')
        return date

    @classmethod
    def year_of_news(cls, strdate):
        date = strdate.split('-')
        return date[0] if date[0] != 'None' else None

    @classmethod
    def month_of_news(cls, strdate):
        date = strdate.split('-')
        if len(date)>1:
            return date[1]

    @classmethod
    def day_of_news(cls, strdate):
        date = strdate.split('-')
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
        count = 0
        for row in reader:
            if row['authors'] == author and row['source_url'] != source_url and row['fake or real'] == 'R':
                count = count + 1
        return count

    @classmethod
    def counter_spelling_mistakes(cls, title, text):
        counter = 0
        for x in title:
            if d.check(x) == False:
                counter = counter + 1
        for x in text:
            if d.check(x) == False:
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
    def if_web_familiar (cls, source_url):
        return None

    @classmethod
    def check_contact_info(cls):
        return False

    @classmethod
    def strange_or_similar_to_large_site(cls):
        return False

    @classmethod
    def check_if_title_extreme_or_not_related_to_text(cls):
        return False

    def get_features_list(self):
        features = []
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

    def __init__(self, params, all_dataset):
        # source_url, date, title, authors, images, text, fake_or_real, all_dataset
        self.title_large_letters_and_exclamation_points = DataFeatures.title_large_letters_and_exclamation_points(params.get('title', ''))
        self.year_of_news = DataFeatures.year_of_news(params.get('date', None))
        self.month_of_news = DataFeatures.month_of_news(params.get('date', None))
        self.day_of_news = DataFeatures.day_of_news(params.get('date', None))
        self.source_url = params.get('source_url','')
        self.number_of_webs_that_publish_this_title = DataFeatures.number_of_webs_that_publish_this_title(params.get('title', ''), params.get('source_url', ''), all_dataset)
        self.authors = params.get('authors', '')
        self.authors_record = DataFeatures.authors_record(params.get('source_url', ''), params.get('authors', ''), all_dataset)
        # self.if_web_familiar = DataFeatures.if_web_familiar(source_url)
        self.counter_spelling_mistakes = DataFeatures.counter_spelling_mistakes(params.get('title', ''), params.get('text', ''))
        self.search_images_gps_source = DataFeatures.gps_images_source(params.get('images', ''))
        self.check_contact_info = DataFeatures.check_contact_info()
        self.strange_or_similar_to_large_site = DataFeatures.strange_or_similar_to_large_site()
        self.check_if_title_extreme_or_not_related_to_text = DataFeatures.check_if_title_extreme_or_not_related_to_text()
        self.fake_or_real = params.get('fake or real','')


if __name__ == '__main__':
    data = []
    with open('../data/fake_data.csv', delimiter='|') as datafile:
        reader = csv.DictReader(datafile)
        for newline in reader:
            source_url = newline['source_url']
            date = newline['date']
            title = newline['title']
            authors = newline['authors']
            images = newline['images']
            text = newline['text']
            fake_or_real = newline['fake or real']
            obj = DataFeatures(source_url, date, title, authors, images, text, fake_or_real, reader)
            data.append(obj)


def bytes_to_float(b):
    return float(crc32(b) & 0xffffffff)


def str_to_float(s, encoding="utf-8"):
    return bytes_to_float(s.encode(encoding))
