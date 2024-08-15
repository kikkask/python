import requests

url = "https://api.opendota.com/api/heroes"
resposta = requests.get(url)

dados = resposta.json()

for i in dados:
  print(i['localized_name'])
