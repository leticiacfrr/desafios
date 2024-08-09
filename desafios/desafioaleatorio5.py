print(' \n Número de Armstrong \n ')
num = str(input('Insira um número inteiro: '))
soma = 0
for char in num:
    n = int(char)
    soma += n**len(num)
print(soma)
if soma == int(num):
    print('O número é um número de Armstrong!')
else:
    print('O número não é um número de Armstrong!')