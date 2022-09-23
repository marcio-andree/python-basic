# continue no python ignora\pula o iteravel
# Exemplo do uso do continue

# for numero in range(100):
#   if numero % 2 == 0:
#     print(numero)
#   else:
#     continue

# # break interrope a iteração assim que a primeira condição for valida

# for i in range(100):
#   if i % 2 == 0:
#     print(i)
#   else:
#     break



# usa operação necessária break ou continue para que as seguinte condição aconteça
# ao chegar no estilo rap o mesmo não deve ser impresso na tela
estilos = ['hip hop', 'rock', 'rap','pop']

for estilo in estilos:
  if estilo == 'rap':

    continue
  print(estilo)



print('############################')

# usa operação necessária break ou continue para que as seguinte condição aconteça
# ao chegar no estilo rock a execução deve ser interrompida
for estilo in estilos:
  if estilo == 'rock':
    break
  print(estilo)
