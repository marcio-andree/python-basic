def saudacao():
  return 'Bem vindo'


print(saudacao())


def media(n1, n2):
  resultado = (n1 + n2 ) / 2
  return resultado

print(media(10,8))

# argumentos com mais de um parametro fixo tem que ser colocado para o final
def conheca_lugar(horario,lugar='nossos pontos turisticos'):
  return print(f'Conheça: {horario, lugar}')


conheca_lugar('16 horas', 'Disney')
