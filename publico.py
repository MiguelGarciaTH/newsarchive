import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from Article import Article


removal_list = ["PUB"]


def get_url(url):
    return requests.post(url)


def get_articles(name, limit):
    url = 'http://arquivo.pt/textsearch?prettyPrint=true&versionHistory=%s&maxItems=%s' % (name, limit)
    response = requests.post(url)
    return json.loads(response.text)


def get_html(url):
    return BeautifulSoup(requests.get(url).text, "html.parser")


def clean_text(text):
    text= text.replace('”','').replace('“','').replace('‘','').replace('’','')
    for word in removal_list:
        text=text.replace(word, "")
    lines = text.splitlines()
    text=''
    for line in lines:
        if "O melhor do Público no email" in line:
            continue
        elif "Continuar a ler" in line:
            continue
        elif "Subscreva gratuitamente as newsletters e receba o melhor da actualidade e os trabalhos mais profundos do Público." in line:
            continue
        elif "×" in line:
            continue
        else:
            text+=line
    return text

def clean_html(soup):
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    html = soup.get_text()
    lines = (line.strip() for line in html.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    return '\n'.join(chunk for chunk in chunks if chunk)


jsonToPython = get_articles('publico.pt', '1000')
list_url = []
print(len(jsonToPython['response_items']))
for i in range(len(jsonToPython['response_items'])):
    intTime = jsonToPython['response_items'][i]['tstamp']
    date = datetime.strptime(intTime, '%Y%m%d%H%M%S').strftime('%d/%m/%Y %H:%M:%S')
    page = get_html(jsonToPython['response_items'][i]['linkToArchive'] + 'opiniao')
    try:
        for link in page.find_all('a'):
            if "noticia" not in link.get('href'):
                continue
            else:
                if any(x in link.get('href') for x in "#?"):
                    continue
                else:
                    list_url.append(tuple([date, 'http:' + link.get('href')]))
    except (TypeError):
        continue

article_list = {}
for elem in list_url:
    article = get_html(elem[1])
    author = article.find('meta', attrs={'name': 'author'})
    date = article.find('time', attrs={'class': 'dateline'})
    text = article.find('div', attrs={'class': 'story__body'})
    text = clean_text(clean_html(text))
    try:
        S = Article(author["content"], text, elem[1], date["datetime"], elem[0])
    except (TypeError):
        continue
    article_list.update({elem[1]:S})

index=0
for elem in article_list.values():
    print(str(index)+", '" + elem.get_text()+"', ?, '"+elem.get_url()+"', '"+elem.get_author()+"'\n")
    index+=1

