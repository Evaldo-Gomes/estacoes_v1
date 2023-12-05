#Estações do Ano
#Apresentação
print('\n\t\t\t  --  Estações do Ano - Simples   --')

#Entradas
mes = input('Informe o mês: ')
dia = int(input('Informe o dia: '))

#Condicional e saída
if mes.lower() == 'janeiro' or mes.lower() == 'fevereiro':
    print(f'Em {dia} de {mes} a estação é Verão!')
elif mes.lower() == 'abril' or mes.lower() == 'maio':
    print(f'Em {dia} de {mes} a estação é Outuno!')
elif mes.lower() == 'julho' or mes.lower() == 'agosto':
    print(f'Em {dia} de {mes} a estação é Inverno!')
elif mes.lower() == 'outubro' or mes.lower() == 'novembro':
    print(f'Em {dia} de {mes} a estação é Primavera!.')

elif mes.lower() == 'março' and dia < 20:
    print(f'Em {dia} de {mes} a estação é Verão!')
elif mes.lower() == 'junho' and dia < 21:
    print(f'Em {dia} de {mes} a estação é Outono!')
elif mes.lower() == 'setembro' and dia < 23:
    print(f'Em {dia} de {mes} a estação é Inverno!')
elif mes.lower() == 'dezembro' and dia < 22:
    print(f'Em {dia} de {mes} a estação é Primavera!')

elif mes.lower() == 'março' and dia >= 20:
    print(f'Em {dia} de {mes} a estação é Outuno!')
elif mes.lower() == 'junho' and dia >= 21:
    print(f'Em {dia} de {mes} a estação é Inverno!')
elif mes.lower() == 'setembro' and dia >= 23:
    print(f'Em {dia} de {mes} a estação é Primavera!')
elif mes.lower() == 'dezembro' and dia >= 22:
    print(f'Em {dia} de {mes} a estação é Verão!')

else:
    print('Dia ou mês incorretos!')