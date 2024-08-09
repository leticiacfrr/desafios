print(' \n POTÊNCIA \n ')
numero2 = ''
while numero2 != 0:
    numero1 = int(input('Insira a base: '))
    numero2 = int(input('Insira o expoente: '))
    print('A potência de {} elevado a {} é {}'.format(numero1, numero2, numero1**numero2))