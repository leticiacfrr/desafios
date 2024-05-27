from random import randint
n = randint(0, 5)
print('JoGo da AdiViNhAçÃo')
chute = int(input('Insira um número entre 0 e 5: '))
if chute == n:
    print('Parabéns! Você acertou!')
else:
    print('Você falhou!')
print('fim')