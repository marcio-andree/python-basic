from array import array

numeros = array('i', [1,2,3,4,5,6])

print(numeros)

numeros.append(7)
print(numeros)

numeros.insert(7,8)
print(numeros)

numeros.pop(0)
print(numeros)

numeros.remove(5)
print(numeros)

del numeros[1]
print(numeros)
