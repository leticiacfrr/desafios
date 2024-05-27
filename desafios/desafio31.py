print('Preço da passagem!')
Km = float(input('Quantos Km são a viagem? '))
if Km < 200:
    valor1 = Km * 0.50
    print('O valor da passagem é de {}'.format(valor1))
else:
    valor2 = Km * 0.45
    print('O valor da passagem é de {}'.format(valor2))