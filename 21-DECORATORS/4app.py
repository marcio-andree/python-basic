from datetime import datetime


def decoratorPrincipal(funcao):
  def horarioAtual():
    print(datetime.now())
    funcao()
    print(datetime.now())

  return horarioAtual

@decoratorPrincipal
def funcaoExecutando():
  print('Estou sendo executado agora')

funcaoExecutando()
