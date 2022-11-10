import random
# gerar um valor aleatório  entre 0.0 a 1.0
print(random.random())

# gera um valor aleatório entre valor inicial e final
print(random.uniform(4, 10))

#gera um valor aleatório entre valor inicial e final inteiro
print(random.randint(1, 100))

# escolher um item dentro aleatório dentro de uma lista

cores = ['blue', 'green', 'yellow', 'orange', 'purple']
print(random.choices(cores, k=2 )) # argumento k=2 permite escolher dois intens dentro da lista

# Embaralhar itens dentro de uma lista

cartas_baralho = ['REI', 'RAINHA', ' VALETE','CORINGA','A']
print(random.shuffle(cartas_baralho))
print(cartas_baralho)

# cara ou coroa
moeda =  ['cara', 'coroa']
print(random.choice(moeda))

# sorteio de lista com 5 participantes
lista_sorteio = ['marcio','juliana','lucas', 'thiago','richard']
print(random.choice(lista_sorteio))

# imprimir um valor aleatório dentre 10-100
print(random.randint(10, 100))
