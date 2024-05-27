print('Limite de velocidade é 80Km/h!')
velocidade = int(input('Qual a sua velocidade? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Vai com calma filhão! Toma aqui sua multa pra ficar esperto {}!'.format(multa))
else:
    print('Tá safe filho! Vai com Deus!')
    