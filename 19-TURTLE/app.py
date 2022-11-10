from turtle import Turtle
t = Turtle()
t.speed(1)

while True:
  distancia = int(input('Digite a distancia a percorrer:'))
  t.forward(distancia)
  continuar = str(input('Deseja continuar a ir para frente ? '))
  if continuar == 's' or continuar == 'S' or continuar == 'sim' or continuar == 'SIM':
    continue
  pass




