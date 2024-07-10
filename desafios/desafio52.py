print ('Números Primos até 100')
n = int(input('Digite o número: '))
total_div = 0
for c in range(1, n + 1):
    if n > 1 and n % c  == 0:
        total_div = total_div + 1
if total_div > 2:
    print ('{} não é um número primo!'.format(n))
else:
    print('{} é um número primo!'.format(n))