import requests

url = "https://api.opendota.com/api/heroes"
dados = requests.get(url).json()

for i in dados:
  print(i['localized_name'])
