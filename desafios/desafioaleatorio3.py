n = input('Digite um número inteiro: ')
print(len(n))
numero_int = int(n)
soma = 0
for c in range(0, len(n)):
    soma += numero_int%10
    numero_int = numero_int//10
print(soma)