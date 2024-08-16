soma_produtos = 0
maior_1000 = 0
contador = 0
menor = 0 
nome_menor = 0
while True:
    nome = input('Nome do produto: ')
    preço = float(input('Preço do produto: '))
    continua = str(input('Quer continuar?[s/n] '))
    while continua != 's' and continua!= 'n':
        continua = str(input('Quer continuar?[s/n] '))
    soma_produtos += preço
    if preço > 1000:
        maior_1000 += 1
    if contador == 0:
        menor = preço
        nome_menor = nome
    if contador >= 1:
        if preço < menor:
            menor = preço
            nome_menor = nome
    contador += 1
    if continua == 'n':
        break
print(f'O total de gastos foi: R${soma_produtos}')
print(f'{maior_1000} foram os produtos custando mais de R$1000')
print(f'O produto mais barato foi: {nome_menor}')