numero = 0
soma = 0
contador = 0
while True:
    numero = int(input('Insira um número: (999 para parar) '))
    if numero == 999:
        break
    soma += numero
    contador +=1
print(f'A quantidade de números digitados foi de {contador} e sua soma é de {soma}')