import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from Article import Article



def get_url(url):
    return requests.post(url)


def get_articles(name, limit):
    url = 'http://arquivo.pt/textsearch?prettyPrint=true&versionHistory=%s&maxItems=%s' % (name, limit)
    response = requests.post(url)
    return json.loads(response.text)


def get_html(url):
    return BeautifulSoup(requests.get(url).text, "html.parser")


def cleanMe(html):
    soup = html
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


jsonToPython = get_articles('publico.pt', '1')
list_url = []
print(len(jsonToPython['response_items']))
for i in range(len(jsonToPython['response_items'])):
    intTime = jsonToPython['response_items'][i]['tstamp']
    date = datetime.strptime(intTime, '%Y%m%d%H%M%S').strftime('%d/%m/%Y %H:%M:%S')
    page = get_html(jsonToPython['response_items'][i]['linkToArchive'] + 'opiniao')
    for link in page.find_all('a'):
        if "noticia" not in link.get('href'):
            continue
        else:
            if any(x in link.get('href') for x in "#?"):
                continue
            else:
                list_url.append(tuple([date, 'http:' + link.get('href')]))

article_list = {}
for elem in list_url:
    article = get_html(elem[1])
    author = article.find('meta', attrs={'name': 'author'})
    date = article.find('time', attrs={'class': 'dateline'})
    text = article.find('div', attrs={'class': 'story__body'})
    text = cleanMe(text)
    S = Article(author["content"], text, elem[1], date["datetime"], elem[0])
    article_list.update({elem[1]:S})

for elem in article_list.values():
    print(elem)

