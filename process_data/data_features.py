import csv


class DataFeatures:

    @classmethod
    def TitleLargeLettersAndExclamationPoints(cls, title):
        if any(x.isupper() for x in title):
            return True
        if title.search('!'):
            return True
        return False

    @classmethod
    def CheckIfRelevantDate(cls, strdate):
        date = strdate.split(' ')
        del date[1]
        date = date[0].split('-')
        return date

    @classmethod
    def IfIncludeAtKnownWebs(cls, title, source_url, reader):
        count = 0
        for row in reader:
            if row['title'] == title and row['source_url'] != source_url:
                count = count + 1
        return count

    @classmethod
    def AuthorsRecord(cls, author):
        for row in reader:
            if row['authors'] == author and row['source_url'] != source_url and row['fake or real'] == 'R':
                count = count + 1
        return count

    @classmethod
    def IfWebFamiliar (cls, source_url):
        return None

    @classmethod
    def IfIncludeSpellingMistakes(cls, title):
        return False

    @classmethod
    def SearchImagesSource(cls,images):
        return False

    @classmethod
    def CheckContactInfo(cls):
        return False

    @classmethod
    def StrangeOrSimilarToLargeSite(cls):
        return False

    @classmethod
    def CheckIfTitleExtremeOrNotRelatedToText(cls):
        return False

    def __init__(self, source_url, date, title, authors, images, fake_or_real, all):
        self.title_large_letters_and_exclamation_points = DataFeatures.TitleLargeLettersAndExclamationPoints(title)
        self.check_if_relevant_date = DataFeatures.CheckIfRelevantDate(date)
        self.if_include_at_known_webs = DataFeatures.IfIncludeAtKnownWebs(title, source_url, all)
        self.authors_record = DataFeatures.AuthorsRecord(title, authors)
        # self.if_web_familiar = DataFeatures.IfWebFamiliar(source_url)
        self.if_include_spelling_mistakes = DataFeatures.IfIncludeSpellingMistakes(title)
        self.search_images_source = DataFeatures.SearchImagesSource(images)
        self.check_contact_info = DataFeatures.CheckContactInfo()
        self.strange_or_similar_to_large_site = DataFeatures.StrangeOrSimilarToLargeSite()
        self.check_if_title_extreme_or_not_related_to_text = DataFeatures.CheckIfTitleExtremeOrNotRelatedToText()
        self.fake_or_real = fake_or_real


if __name__ == '__main__':
    data = []
    with open('../data/my_data.csv') as datafile:
        reader = csv.DictReader(datafile)
        for row in reader:
            source_url = row['source_url']
            date = row['date']
            title = row['title']
            authors = row['authors']
            images = row['images']
            fake_or_real = row['fake or real']
            obj = DataFeatures(source_url, date, title, authors, images, fake_or_real, reader)
            data.append(obj)
