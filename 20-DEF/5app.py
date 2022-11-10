# **kwargs recebe mais um valor nomeado

def concaternar(**words):
  frase = ''
  for word in words.values():
    frase += word + ' '
  print(frase)

concaternar(a='aprendendo', b='funcões', c='**kwargs', d='em python')
