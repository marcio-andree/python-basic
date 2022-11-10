# importando as requisições
import requests
# API para cotar o dolar
url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
#busca os dados
response = requests.get(url)
# condição para mostrar a cotação do dolar
if response.status_code == 200:
   dolar_value = response.json()['USD']['low']
   print(f'O valor atual do Dolar é $ {dolar_value}')
else:
  print(f'Erro ao buscar valor do Dolar')
