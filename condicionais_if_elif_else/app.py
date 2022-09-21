trabalho_terminado = False

if trabalho_terminado == True:
    print(' trabalho concluído! Bora dar um rolê')
else:
    print('terminar o trabalho')


# Receba a velocidade de um carro e verifique se se está dentro das normas ou não
# a velocidade máxima permitida é de 50km
# se velocidade igual a 50km está andando com segurança boa viagem
# cruzou entre 51km a 60km , levou multa de 2 pontos
# cruzou entre 61km a 75km, levou multa de 3 pontos
# cruzou entre 75km e 100km levou multa de 7 pontos


velocidade = int(input('Digite a velocidade do carro:'))
if velocidade <= 50:
  print('Está andando com segurança boa viagem')
elif velocidade >= 51 and velocidade <= 60:
  print('cruzou a cima de de 51 multa de 2 pontos')
elif velocidade >= 61 and velocidade <= 75:
  print('cruzou a cima de de 61 multa de 7 pontos')
else:
  print('Perdeu o direito de dirigir')

corte = float(input('Digite o tamanho do seu cabelo em centimetros: '))
if corte <= 20:
  print('O valor para esse corte é R$ 50,00 reais: ')
elif  corte >= 21 and corte <= 30:
  print('O valor para esse corte é R$ 70,00 reais: ')
elif corte >= 31 and corte <= 50:
  print('O valor para esse corte é R$ 100,00 reais: ')
else:
  print('Consulte o valor do corte na recepção')

# resolução a versão chaining

valor_corte = float(input('Digite o tamanho do cabelo em cm: '))

if valor_corte <= 20:
  print('O valor para esse corte é R$ 50,00 reais: ')
elif 21 <= valor_corte <= 30:
   print('O valor para esse corte é R$ 70,00 reais: ')
elif 31 <= valor_corte <= 50:
  print('O valor para esse corte é R$ 100,00 reais: ')
else:
  print('Consulte o valor do corte na recepção')


