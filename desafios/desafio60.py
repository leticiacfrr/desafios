contador = int(input('Insira um número inteiro: '))
fatorial = 1
while contador > 0 :
    if contador > 1:
        print('{} x '.format(contador), end = '')
    else:
        print('{} = {}'.format(contador, fatorial))
    fatorial = contador * fatorial
    contador = contador - 1
