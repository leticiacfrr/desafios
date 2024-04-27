from math import sin,cos,tan,radians
print('Calculando o seno, cosseno e tangente de um ângulo')
ang = int(input('Insira um ângulo: '))
sen = sin(radians(ang)) #esta formula é para radianos
coss = cos(radians(ang)) 
tg = tan(radians(ang))
print('O valor do seno, cosseno e tangente são respectivamentes {:.2f}, {:.2f} e {:.2f}'.format(sen, coss, tg))