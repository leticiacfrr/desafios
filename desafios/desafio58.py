print('JoGo da AdiViNhAçÃo')
from random import randint
n = randint(0, 10)
contador = 0
chute = int(input('Insira um número entre 0 e 10: '))
while n != chute:
    chute = int(input('Insira um número entre 0 e 10: '))
    contador = contador + 1
print('Você acertou! A quantidade de erros foi {}'.format(contador))
