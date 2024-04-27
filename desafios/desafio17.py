import math
print('Calculando o valor da hipotenusa de um triângulo retângulo')
catop = float(input('Insira o valor do cateto oposto: '))
catad = float(input('Insira o valor do cateto adjacente: '))
hip = math.sqrt((math.pow(catop,2) + math.pow(catad,2)))
print('O valor da hipotenusa é de {}'.format(hip))