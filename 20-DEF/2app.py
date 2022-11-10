def cotacaoDolar(moeda):
  if moeda == 'usd':
    return 5.13
cotacao = cotacaoDolar('usd')
if cotacao < 5.50:
  print('Investir no Dolar')
else:
  print('Cotação do dolar a cima do favoravel')



