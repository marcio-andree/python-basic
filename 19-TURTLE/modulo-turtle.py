# como usar o modulo turtle
# para fazer importação basta digitar from turtle import Turtle
from turtle import Turtle

# para iniciarlizar o modulo usamos Turtle()
t = Turtle()


# Definir a velocidade do movimento t.speed() argumento pode receber de 1 a 10
t.speed(1)

# para movimentar para frente t.forward(100)
t.forward(100)

# rotacionar em X graus para direita t.right(90)
t.right(90)
t.forward(100)

# rotacionar em X graus para para esquerda t.left(90)
t.left(90)
t.forward(100)

# Movimentar para trás t.backward(100)
t.back(200)
input()
