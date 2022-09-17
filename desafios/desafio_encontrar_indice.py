# desafio 1
# Encontre o indice de 'o' dentro da variável biblioteca
biblioteca = 'Biblioteca'
print(biblioteca.index('o'))

# Desafio 2
# imprima apenas 'De Aplicações'
frase = 'Desenvolvimento de Aplicações'
indice_d = frase.rindex('d')
indice_s = frase.rindex('s')

print(frase[indice_d : indice_s + 1]) # como python ignora o ultima indice é necessário acrescentar o +1 para que ele vá até ofinal da posição
