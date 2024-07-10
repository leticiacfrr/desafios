print('Maior idade!')
maior = 0
menor = 0
for d in range(0, 7):
    ano_nasc = int(input('insira seu ano de nascimento completo: '))
    if ano_nasc >= 2003:
        maior = maior + 1
        menor = 7 - maior
print('{} são maiores e {} ainda não atingiram a maior idade!'.format(maior, menor))