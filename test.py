import requests
from bs4 import BeautifulSoup
from WekaFile import WekaFile
import re

weka = WekaFile("train_data", "train")
weka.write_template()


url="http://www.psd.pt/noticias/"
index=0 #697
for i in range(1,697):
    page = BeautifulSoup(requests.get(url+str(i)).text, "html.parser")
    productDivs = page.findAll('div', attrs={'class': 'titulo_noticia'})
    for div in productDivs:
        article = BeautifulSoup(requests.get(div.find('a')['href']).text, "html.parser")
        text = article.find('div', attrs={'class': 'item_interior_texto_grande'}).findAll('p', attrs={'style': 'text-align:justify'})
        article_text = ''
        index += 1
        for element in text:
            article_text += ''.join(element.findAll(text=True))
        if len(article_text) > 0:
            weka.write(index, article_text, "D")

weka.close()