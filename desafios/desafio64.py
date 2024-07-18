n = 0
soma = 0
contador = 0
while n != 999:
    n = int(input('Insira um número: '))
    contador = contador + 1
    #print(contador)
    if contador >= 2:
        soma += n
        #print(soma)
print('A quantidade de número digitados foi {} e a soma de todos eles foi {}'.format(contador, soma - 999))