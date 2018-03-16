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


jsonToPython = get_articles('publico.pt', '1')

print(len(jsonToPython['response_items']))
for i in range(len(jsonToPython['response_items'])):
    intTime = jsonToPython['response_items'][i]['tstamp']
    date = datetime.strptime(intTime, '%Y%m%d%H%M%S').strftime('%d/%m/%Y %H:%M:%S')
    print(date + ' ' + jsonToPython['response_items'][i]['linkToArchive'])
    print('Opinioes: ' + jsonToPython['response_items'][i]['linkToArchive']+'opiniao')
#    print(get_url(jsonToPython['response_items'][i]['linkToArchive']+'opiniao').text)


r  = requests.get(jsonToPython['response_items'][i]['linkToArchive']+'opiniao')
data = r.text
soup =  BeautifulSoup(data, "html.parser")

for link in soup.find_all('a'):
    if "noticia" not in link.get('href'):
        continue
    else:
        print(link.get('href'))
