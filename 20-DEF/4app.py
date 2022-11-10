
# função que recebe mais um valor com argumento posicional
# é chamada de *args

def somar(*valores, valor2):
  for valor in valores:
    valor2 += valor
  return valor2

print(somar(10,10,10, valor2=10))
