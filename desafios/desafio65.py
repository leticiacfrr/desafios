num = 0
media = 0
contador = 0
escolha = 's'
while escolha != 'n':
    num = int(input('Insira um número: '))
    escolha = input('Você quer continuar? [s/n]: ')
    media += num
    if contador == 0:
        maior = num 
        menor = num
    if contador >= 1:
        if num > maior:
            maior = num
            
        elif num < menor:
            menor = num
    contador = contador + 1
print('A media dos números foi de {}, e o maior e menor número são: {}, {}'.format(media/contador, maior, menor))