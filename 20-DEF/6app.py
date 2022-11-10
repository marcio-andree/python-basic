def calculo(nome, *args, **kwargs):
  print(nome)
  print(args)
  print(kwargs)
  for arg in args:
    print(arg)
  for kwarg in kwargs.values():
    print(kwarg)


calculo('Marcop', 10,10,10, a=1, b=2, c=3, d=4)
