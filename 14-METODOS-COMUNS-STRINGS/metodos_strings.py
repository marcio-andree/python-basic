nome_curso = ' Edição de Vídeo '
print(nome_curso.upper()) # transforma tudo em maiusculo
print(nome_curso.lower()) # transforma tudo em minusculo
print(nome_curso.strip()) # remove os espaços em branco
print(nome_curso.lstrip()) # remove os espaços em branco somente da esqueda
print(nome_curso.rstrip()) # remove os espaços em branco somente da direita
print(nome_curso.find('çao')) # mostra a posição do indice da palavra string
print(nome_curso.replace('Vídeo', 'Música')) # substitui a primeira string pela segunda string


# exemplo de como pode ser usado
# substitui carros na pesquisa do olx por cachorros
print('https://es.olx.com.br/?q=carros'.replace('carros', 'cachorros'))
print('https://es.olx.com.br/?q=carros'.replace('carros', 'apartamentos'))
