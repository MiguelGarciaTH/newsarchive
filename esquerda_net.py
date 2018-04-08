import requests
from bs4 import BeautifulSoup
from WekaFile import WekaFile


url="https://www.esquerda.net/artigos/6?page="
main_url="https://www.esquerda.net/"
index=0
weka = WekaFile("esquerda_net", "esquerdanet")
weka.write_template()
for i in range(0,100):
    page = BeautifulSoup(requests.get(url+str(i)).text, "html.parser")
    productDivs = page.findAll('div', attrs={'class': 'ver-mais-lista'})
    for div in productDivs:
        article = BeautifulSoup(requests.get(main_url+div.find('a')['href']).text, "html.parser")
        text = article.find('div', attrs={'class': 'field field-name-body'}).findAll('p')
        article_text = ''
        index+=1
        for element in text:
            article_text += ''.join(element.findAll(text=True))
        #print(str(index)+", '"+ article_text.replace('"','')+ "', "+ "E, '" +main_url+div.find('a')['href']+"'\n")
        weka.write(index, article_text.replace('"',''), "E")

weka.close()