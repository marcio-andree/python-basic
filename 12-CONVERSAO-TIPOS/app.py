idade = input(' Qual éa sua idade? ')
# print(idade > 18)
# TypeError: '>' not supported between instances of 'str' and 'int'
# esse erro é apresentado porque estamos tentando comparar uma valor string (texto) com um valor inteiro número
# por padrão senão tipartamos o valor de entrada o paython trata como string

# forma para converter strin em inteiro
print(int(idade) > 18)

#forma para converter inteiro em string
print(type(str(5)))
