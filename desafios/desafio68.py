from random import randint
print('PAR OU IMPAR \n')
numero = 0
contador = 0
soma = 0
while True:
    escolha = str(input('Você escolhe par ou ímpar? [p/i] '))
    numero = int(input('Insira seu número: [0, 10] '))
    numero_pc = (randint(0, 10))
    print(numero_pc)
    soma = numero + numero_pc
    if soma % 2 == 0 and escolha == 'p':
        print('VITÓRIA!')
        contador +=1
    elif soma % 2 != 0 and escolha == 'i':
        print('VITÓRIA!')
        contador +=1
    else:
        break
print(f'DERROTA! Essa é sua quantidade de vitórias {contador}')