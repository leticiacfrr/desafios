print('Jogo da adivinhação')
from random import randint
n = randint(1 ,100)
num = int(input('Adivinhe o número: '))
while (num != n):
    if num > n:
        print('muito alto')
        num = int(input('Adivinhe o número: '))
    elif num < n:
        print('muito baixo')
        num = int(input('Adivinhe o número: '))
print('Acertou!', n)
