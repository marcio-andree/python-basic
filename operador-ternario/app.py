# caso a idade for maior ou igual a 18 anos a pessoa é maior de idade caso contrário ela é menor de idade

idade = 15
if idade >= 18:
  print(' maior de idade')
else:
  print(' menor de idade')

# usando agora operador ternário
idade1 = 18
print('maior de idade') if idade >= 18 else print('menor de idade')

# se velocidade acima de 100 exibir "você foi multado" caso contrário exiba siga em frente
velocidade = 101
print('você foi multado') if velocidade >= 100 else print('siga em frente')
