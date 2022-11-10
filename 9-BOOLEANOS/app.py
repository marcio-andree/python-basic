# idade = 18
# convite = True
# reserva = True

# print((idade >= 18 and convite == True) and (reserva  == False))

possui_passaporte = False
passagem_comprada = True
menor_de_idade = False

# desafio 1 uma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada e não for menor de idade
print((possui_passaporte and passagem_comprada) and  not menor_de_idade)

# desafio 2 uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
print((possui_passaporte or passagem_comprada) and not menor_de_idade)

# desafio 3 uma pessoa se não possui passaporte ou tiver a passagem comprada e não for menor de idade
print((not possui_passaporte or passagem_comprada) and not menor_de_idade)
# desafio 4 uma pessoa não pode viajar senão possuir um passaporte ou não tiver a passagem comprada e for menor de idade
print((not possui_passaporte or passagem_comprada) and menor_de_idade)
