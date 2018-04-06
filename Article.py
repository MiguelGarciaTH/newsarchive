class Article(object):

    def __init__(self, author, text, url, date, archive_date):
        self.url = url
        self.date = date
        self.author = author
        self.archive_date = archive_date
        self.text = text

    def get_url(self):
        return self.url

    def get_author(self):
        return self.author

    def get_published_date(self):
        return self.date

    def get_text(self):
        return self.text

    def get_archive_date(self):
        return self.archive_date

    def __str__(self):
        return "Author: "+ self.author + "\nText:" +self.text+"\nUrl:" +self.url+"\nDate:" + self.date  + "\nPublished date:"+ self.archive_date

