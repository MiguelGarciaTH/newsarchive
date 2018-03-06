import requests

url = 'http://arquivo.pt/textsearch?q=Albert%20Einstein&maxItems=5&prettyPrint=true'
response = requests.post(url)
print response.text