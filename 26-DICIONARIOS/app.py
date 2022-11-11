# dicionário usa chave e valor

pessoa1 = {
            'nome':'Caramelinho',
            'idade':8,
            'altura':120
};
# outra forma de criar dicionário
pessoa2 = dict(nome='Caramelão', idade=15, altura=160);
print(pessoa1);
print(pessoa2);

# acessando propriedade do diciário atráves da chave

print(pessoa1['nome'])

# acesando a chaves diponiveis em um dicionário
print(pessoa1.keys())
print(pessoa1.values())
print(pessoa1.items())

for item in pessoa1.items():
  print(item)
  print(item[1])
