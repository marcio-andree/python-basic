# tranformes a strigs de foma dinâmica
# feito é MELHOR QUE perfeito
# Resultado esperado: É melhor FEITO QUE PERFEITO
a = 'é'
b = 'MELHOR'
c = 'QUE'
d = 'feito'
e = 'perfeito'

a = a.upper()
d = d.upper()
c = c.upper()
e = e.upper()
b = b.lower()

frase = a, b, c, d, e,

print(frase)
print(f'{a} {b} {d} {c} {e}')

