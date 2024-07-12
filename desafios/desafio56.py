media = 0
velho = 0
nome_velho = 0
mulher_menor_20 = 0
for m in range (0, 4):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: '))
    media += idade
    if sexo == 'f' and idade < 20:
       mulher_menor_20 =mulher_menor_20 + 1 #contador salva o dado por si só
    if sexo == 'm':
        if m == 0:
         velho = idade
         nome_velho = nome
        if idade > velho:
            velho = idade
            nome_velho = nome
print('O nome do homen mais velho é {}'.format(nome_velho))
print('A quantidade de mulheres com menos de 20 anos é {}'.format(mulher_menor_20))
print('A media é {}'.format(media/4))