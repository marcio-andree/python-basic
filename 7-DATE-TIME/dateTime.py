from datetime import datetime
print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data
viagem_marte = datetime(2030, 5, 10)
print(viagem_marte)
# recebendo a data do usuário formato string
#data_niver = input('Digite sua data de aniversário:')
#print(data_niver)

# recebendo a data do usuário e transformando para classe datetime
# OBS o Y no final é maisculo pois representa 4 digitos do ano

data_lacamento = datetime.strptime(input('Digite a data de lançamento DIA/MES/ANO: '), '%d/%m/%Y')
print(type(data_lacamento))
# calcular o interno entre datas
data_atual = datetime.now()
prazo = data_lacamento - data_atual
print(f'O prazo para o laçamento da da Falcon 9 é de {prazo.days} dias')

# calculadora de data de aniversário
aniversario = datetime(2023, 1, 8)
dias_para_aniversario = aniversario - datetime.now()
print(f'Faltam {dias_para_aniversario.days} dias para o aniversário')

