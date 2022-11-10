valores = [1,2,3,4,5,6,7,8,9,10]
print(valores)

anos = [2020,2030,2040,2050,2060]
# append() adiciona um valor ao final da lista
valores.append(11)
print(valores)

# unir listas extend()
valores.extend(anos)
print(valores)


# inserir um valor em uma posição expecifica na lista insert()

anos.insert(3,2045)
print(anos)

# extrair uma infomação sem apaga-la da lista pop()
ano2060 = anos.pop(4)
print(ano2060)

# apagar um item da lista pelo valor remove
anos.remove(2045)
print(anos)

# apagar uma item da lista pelo índice del []
del anos[0]
print(anos)


# apagar uma faixa de valores da lista pelo índice del [2:6]
valores_2 = [1,2,3,4,5,6,7,8,9,10]
print(valores_2)
del valores_2[2:6]
print(valores_2)

# contar as ocorrencias dentro de uma lista
nomes =['gabi','pedro','arraca','gabi','everton','thiago']
print(nomes.count('gabi'))


# apagar todos os itens da lista clear()
valores_3 = [1,2,3,4,5,6,7,8,9,10]
print(valores_3)
valores_3.clear()
print(valores_3)
