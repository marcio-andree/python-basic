# Metodo Slip separa uma frase em palavras obs o separador não é incluido na lista final
frase = 'olá, bem-vindo eu sou python seu melhor amigo'
print(frase.split())
print(frase.split('-')) # se para as strings quando encontrar um traço

nomes = 'malagotti,macabias,joquebe,jorias'
print(nomes.split(','))

hashiteg = '#music#guitar#play#pause#headphones#chair'

print(hashiteg.split('#',3)) # parametro de inicio e ocorre até a terceiro item na lista

print(hashiteg.split('#'))

# join junta os espaços com o catacter que você pedir
hashiteg2 ='#python #postgresql #html #php #sql'
hashiteg2_join =hashiteg2.split(' ')
print(','.join(hashiteg2_join))
print('-'.join(hashiteg2_join))

# Desafio 1 transforme a frase 1 em uma lista de palavras depois guarda o rsultado em uma varivel chamada palvras 1
frase1 = 'Desafio manipulação de Strings'
frase2 = 'jhonan, rafael, carol, camilla'
palavras1 = frase1.split()
# Desafio 2 transformar a frase 2 em uma lista de palavras
palavras2 = frase2.split(',')
# desafio 3 pegue o palavras 1 e transforme elas no seguinte : "Desafio manipulçaõ,de, string" imprime o resultado no console
print(','.join(palavras1))
# desafio 4 pegue o palvras2 e transforme elas no seguinte string: frase2 =
# jhonan &  rafael &  carol &  camilla
print(' & '.join(palavras2))

