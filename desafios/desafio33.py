print('Maior Menor')
n1 = float(input('Insira um número: '))
n2 = float(input('Insira um número: '))
n3 = float(input('Insira um número: '))
if n1 > n2 and n1 > n3:
    print('{} é o maior valor!'.format(n1))
elif n2 > n3:
    print('{} é o maior valor!'.format(n2))
else:
    print('{} é o maior valor!'.format(n3))
if n1 < n2 and n1 < n3:
    print('{} é o menor valor!'.format(n1))
elif n2 < n3:
    print('{} é o menor valor!'.format(n2))
else:
    print('{} é o menor valor!'.format(n3))