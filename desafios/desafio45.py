from random import choice
escolhapc = choice (['pedra', 'papel', 'tesoura'])
escolhape = str(input('pedra, papel, tesoura: '))
if escolhape == 'pedra'or escolhape == 'papel' or escolhape == 'tesoura':
    if escolhapc == 'pedra' and escolhape == 'tesoura':
        print('Você perdeu! Pc: {}. Pe: {}'.format(escolhapc, escolhape))
    elif escolhapc == 'tesoura' and escolhape == 'papel':
        print('Você perdeu! Pc: {}. Pe: {}'.format(escolhapc, escolhape))
    elif escolhapc == 'papel' and escolhape == 'pedra':
        print('Você perdeu! Pc: {}. Pe: {}'.format(escolhapc, escolhape))
    elif escolhape == 'tesoura' and escolhapc == 'papel':
        print('Você ganhou! Pc: {}. Pe: {}'.format(escolhapc, escolhape))
    elif escolhape == 'pedra' and escolhapc == 'tesoura':
        print('Você ganhou! Pc: {}. Pe: {}'.format(escolhapc, escolhape))
    elif escolhape == 'papel' and escolhapc == 'pedra':
        print('Você ganhou! Pc: {}. Pe: {}'.format(escolhapc, escolhape))
    else:
        print('Empate! Pc: {}. Pe: {}'.format(escolhapc, escolhape))
else:
    print('Escolha inválida!')