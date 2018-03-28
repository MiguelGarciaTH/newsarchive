class Article(object):

    def __init__(self, author, text, url, date, archive_date):
        self.url = url
        self.date = date
        self.author = author
        self.archive_date = archive_date
        self.text = text


    def __str__(self):
        return "Author: "+ self.author + "\nText:" +self.text+"\nUrl:" +self.url+"\nDate:" + self.date  + "\nPublished date:"+ self.archive_date

