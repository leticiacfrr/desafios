ano_nasc = int(input('Insira o ano de seu nascimento: '))
idade = 2024 - ano_nasc
if idade > 18:
    n1 = idade - 18
    print('Você já passou {} anos da idade de se alistar!'.format(n1))
elif idade < 18:
    n2 = 18 - idade
    print('Falta(m) {} ano(s) para você se alistar!'.format(n2))
else:
    print('Você já está na idedae de se alistar!')