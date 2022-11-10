ex1 = 'Teclado Teclado Teclado Teclado Teclado'
print(ex1[2]) # chaves é forma como acessamos a posição de uma string pyhton sempre incia contagem com 0
print(ex1[4])
print(ex1[-1]) # -1 retorna a a posição da ultima letra dentro da string

ex2 = 'Teclado'
print(ex2.index('o')) # index retona o indice da letra dentro da string
print(ex2[ex2.index('l')])

# retona partes dentro de uma string seguindo o indice informado sempre conta a posição inicial -1

link = 'http://www.google.com'
print(link[0])
print(link[1])
print(link[0:5])
print(link[0:7]) # retonar o indice na posição 0 até 6 o número final sempre é ignorado
print(link[-5:]) # vai até fim da string e volta 5 indices
print(link[5:]) # caso não especifique ele busca do inicio da posição indica até o final
print(link[5:10]) # 5 indica inicio da posição 10 indica o final sempre ignorando o ultimo número

ex3 = 'Clean Code'
print(ex3.rindex('C')) # acessa a última ocorrencia de um caracter dentro de uma string

