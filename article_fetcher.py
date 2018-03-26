import json
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def get_url(url):
    return requests.post(url)


def get_articles(name, limit):
    url = 'http://arquivo.pt/textsearch?prettyPrint=true&versionHistory=%s&maxItems=%s' % (name,limit)
    response = requests.post(url)
    return json.loads(response.text)


def get_html(url):
    return BeautifulSoup(requests.get(url).text, "html.parser")


jsonToPython = get_articles('publico.pt', '1')
list_articles=[]
print(len(jsonToPython['response_items']))
for i in range(len(jsonToPython['response_items'])):
    intTime = jsonToPython['response_items'][i]['tstamp']
    date = datetime.strptime(intTime, '%Y%m%d%H%M%S').strftime('%d/%m/%Y %H:%M:%S')
#    print(date + ' ' + jsonToPython['response_items'][i]['linkToArchive'])
    page = get_html(jsonToPython['response_items'][i]['linkToArchive']+'opiniao')
    for link in page.find_all('a'):
        if "noticia" not in link.get('href'):
            continue
        else:
            if any(x in link.get('href') for x in "#?"):
                continue
            else:
                list_articles.append(tuple([date,'http:'+link.get('href')]))


for elem in list_articles:
    print(elem[0] + ' ' + elem[1])
    article = get_html(elem[1])
    author =article.find('meta', attrs = {'name':'author'})
    text = article.find('div', attrs = {'class': 'story__body'})
    print(author["content"])
