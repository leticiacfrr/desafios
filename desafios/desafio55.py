print('Peso!')
gordo = 0
magro = 0
for p in range(0, 5):
    peso = float(input('insira seu peso(kg): '))
    if p == 0:
        gordo = peso
        magro = peso
    elif gordo < peso:
        gordo = peso
    elif magro > peso:
        magro = peso
print('O {} é o mais pesado e {} é o menos.'.format(gordo, magro))