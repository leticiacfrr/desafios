divisão50 = 0
subtração50 = 0
divisão20 = 0
subtração20 = 0
divisão10 = 0
subtração10 = 0
divisão1 = 0
subtração1= 0
while True:
    print('\nBEM VINDO AO BANCO L\n')
    numero = int(input('Quanto deseja retirar: R$'))
    print('\n')
    divisão50 = numero // 50
    subtração50 = numero - (divisão50*50)
    divisão20 = subtração50 // 20
    subtração20 = subtração50 - (divisão20*20)
    divisão10 = subtração20 // 10
    subtração10 = subtração20 - (divisão10*10)
    divisão1 = subtração10 // 1
    subtração1 = subtração10 - (divisão1*1)
    if subtração1 == 0:
        print(f'São {divisão50} notas de R$50,00')
        print(f'São {divisão20} notas de R$20,00')
        print(f'São {divisão10} notas de R$10,00')
        print(f'São {divisão1} notas de R$1,00')
        print(f'\nVolte Sempre!\n')
        break
    else:
        print('FALHOU!')