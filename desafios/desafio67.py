numero = 0
while True:
    numero = int(input('Digite um número: '))
    resultado = 0
    if numero >= 0:
        for tabuada in range(0, 11):
            resultado = numero * tabuada
            print(f'{numero} x {tabuada} = {resultado}')
    else:
        break
print('Obrigada por se divertir conosco, volte sempre!')