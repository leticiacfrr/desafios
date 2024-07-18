escolha = 0
valor1 = float(input('Insira um valor: '))
valor2 = float(input('Insira um valor: '))
print(' ')
print('Os valores são {} e {} '.format(valor1, valor2))
while escolha != 5:
    print('Escolha a opção:')
    print('1. Soma;')
    print('2. Multiplicação;')
    print('3. Maior;')
    print('4. Novos valores;')
    print('5. Sair do programa.\n')
    escolha = int(input('Insira o Número da opção desejada: '))
    print(' ')
    if escolha == 1:
        soma = valor1 + valor2
        print('A soma dos valores é de {} \n'.format(soma))
    elif escolha == 2:
        multiplicação = valor1 * valor2
        print('A multiplicação dos valores é de {} \n'.format(multiplicação))
    elif escolha == 3:
        if valor1 > valor2:
            print('O maior valor é {} \n'.format(valor1))
        elif valor1 == valor2:
            print('Os valores são iguais!')
        else:
            print('O maior valor é {} \n'.format(valor2))
    elif escolha == 4:
        valor1 = float(input('Insira um valor: '))
        valor2 = float(input('Insira um valor: '))
        print('Os novos valores são {} e {} \n'.format(valor1, valor2))
    else:
        print('Programa encerrado!')