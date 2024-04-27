print('Jogo da adivinhação')
from random import randint
chutepc = randint(1 ,100)
eleacertou = "não"
chutepcmaior = 100
chutepcmenor = 1
print('Qual o seu chute? ',chutepc)
eleacertou = str(input('Eu acertei?' ))
if (eleacertou == 'n'):
    dica = str(input('Fala minha dica: '))
while (eleacertou != "s"):
    if (dica == 'maior'):
        chutepcmaior = chutepc
    elif (dica == 'menor'):
        chutepcmenor = chutepc
    chutepc = randint(chutepcmenor, chutepcmaior)
    print('Qual o seu chute? ',chutepc)    
    eleacertou = str(input('Eu acertei?' ))
    if(eleacertou == 'n'):
        dica = str(input('Fala minha dica: '))
print('Uhuul! sou um gênio!')


