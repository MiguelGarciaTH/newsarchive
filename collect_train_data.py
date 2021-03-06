import requests
from bs4 import BeautifulSoup
from WekaFile import WekaFile
import re

weka = WekaFile("train_data", "train")
weka.write_template()
global_index=0
#ESQUERDA_NET
url="https://www.esquerda.net/artigos/6?page="
main_url="https://www.esquerda.net/"
index=0
for i in range(0,100):#100
    page = BeautifulSoup(requests.get(url+str(i)).text, "html.parser")
    productDivs = page.findAll('div', attrs={'class': 'ver-mais-lista'})
    for div in productDivs:
        article = BeautifulSoup(requests.get(main_url+div.find('a')['href']).text, "html.parser")
        text = article.find('div', attrs={'class': 'field field-name-body'}).findAll('p')
        article_text = ''
        index+=1
        global_index+=1
        for element in text:
            article_text += ''.join(element.findAll(text=True))
        if len(article_text) > 0:
            weka.write(global_index, article_text, "E")

#PSD
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
        global_index += 1
        for element in text:
            article_text += ''.join(element.findAll(text=True))
        if len(article_text) > 0:
            weka.write(global_index, article_text, "D")

#PS
url="http://www.ps.pt/category/imprensa/opiniao/page/"
index=0 #15
for i in range(1,15):
    page = BeautifulSoup(requests.get(url+str(i)).text, "html.parser")
    productDivs = page.findAll('h4', attrs={'class': 'title has-image'})
    for div in productDivs:
        article = BeautifulSoup(requests.get(div.find('a')['href']).text, "html.parser")
        text = article.find('div', attrs={'class': 'entry-content'})
        text = re.sub(r'\([^)]*\)', '', text.get_text())
        global_index += 1
        weka.write(global_index, text, "E")

weka.close()