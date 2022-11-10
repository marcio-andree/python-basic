def meu_decorator(funcao):
  def wrapper():
    print('Executado antes')
    funcao()
    print('Executado depois')

  return wrapper


@meu_decorator
def parabenizar():
  print('parabens')


parabenizar()
