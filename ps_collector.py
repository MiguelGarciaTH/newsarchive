import requests
from bs4 import BeautifulSoup
import re

url="http://www.ps.pt/category/imprensa/opiniao/page/"
index=0 #697
for i in range(1,15):
    page = BeautifulSoup(requests.get(url+str(i)).text, "html.parser")
    productDivs = page.findAll('h4', attrs={'class': 'title has-image'})
    for div in productDivs:
        article = BeautifulSoup(requests.get(div.find('a')['href']).text, "html.parser")
        text = article.find('div', attrs={'class': 'entry-content'})
        text = re.sub(r'\([^)]*\)', '', text.get_text())
        print(str(index)+ " " +text+ "\nEND\n\n")

        #article_text = ''
        index += 1
        #for element in text:

      #      article_text += ''.join(element.findAll(text=True))
      #  if len(article_text) > 0:
      #      weka.write(index, article_text, "D")

