from datetime import datetime
import requests
from bs4 import BeautifulSoup


url="https://www.esquerda.net/artigos/6?page="
main_url="https://www.esquerda.net/"
index=0
for i in range(0,1):
    page = BeautifulSoup(requests.get(url+str(i)).text, "html.parser")
    productDivs = page.findAll('div', attrs={'class': 'ver-mais-lista'})
    for div in productDivs:
        article = BeautifulSoup(requests.get(main_url+div.find('a')['href']).text, "html.parser")
        text = article.find('div', attrs={'class': 'field field-name-body'}).findAll('p')
        article_text = ''
        index+=1
        for element in text:
            article_text += ''.join(element.findAll(text=True))
        print(str(index)+", '"+ article_text.replace('"','')+ "', "+ "E, '" +main_url+div.find('a')['href']+"'\n")
