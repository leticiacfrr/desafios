n = int(input('Insira um número inteiro: '))
f, f1 = 0, 1
contador = 0
while contador < n:
    print(f, end=' ')
    f, f1 = f1, f + f1
    contador = contador + 1
