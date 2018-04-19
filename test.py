import requests
from bs4 import BeautifulSoup
url="http://www.psd.pt/noticia/"


article = BeautifulSoup(requests.get(url+str(2910)).text, "html.parser")
text = article.find('div', attrs={'class': 'item_interior_texto_grande'}).findAll('p')
print(text)
article_text = ''
for element in text:
    article_text += ''.join(element.findAll(text=True))
print(article_text.replace('\t','').replace('\n','').replace('  ', ''))