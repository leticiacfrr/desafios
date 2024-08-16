maior_18 = 0
homens = 0
mulheres_menor_20 = 0
while True:
    print('\n Cadastrando pessoas \n')
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo?[m/f] '))
    while sexo != 'f' and sexo != 'm':
        sexo = str(input('Qual o sexo?[m/f] '))
    continua = str(input('Quer continuar?[s/n] '))
    while continua != 's' and continua!= 'n':
        continua = str(input('Quer continuar?[s/n] '))
    if idade > 18:
        maior_18 += 1
    if sexo == 'm':
        homens += 1
    if idade < 20 and sexo == 'f':
        mulheres_menor_20 += 1
    if continua == 'n':
        break
print(f'A quantidade de maiores de 18 anos cadastrados é: {maior_18}')
print(f'A quantidade de homens cadastrados é: {homens}')
print(f'A quantidade de mulheres menores de 20 anos cadastradas é: {mulheres_menor_20}')