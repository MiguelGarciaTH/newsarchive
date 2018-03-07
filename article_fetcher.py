import requests
import json
from datetime import datetime



def get_articles(name, limit):
    url = 'http://arquivo.pt/textsearch?prettyPrint=true&versionHistory=%s&maxItems=%s' % (name,limit)
    response = requests.post(url)
    return json.loads(response.text)


jsonToPython = get_articles('publico.pt', '1')
intTime = jsonToPython['response_items'][0]['tstamp']
date = datetime.strptime(intTime, '%Y%m%d%H%M%S').strftime('%d/%m/%Y %H:%M:%S')


print(date + ' ' + jsonToPython['response_items'][0]['linkToArchive'])


