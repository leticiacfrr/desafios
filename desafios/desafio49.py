n = int(input('Digite um número para ver sua tabuada: '))
r = 0
for t in range(0, 10+1):
    r = n * t 
    print('{} x {} = {}'.format(n, t, r))