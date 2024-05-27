print('Forma um triângulo?')
r1 = float(input('Insira o valor da reta: '))
r2 = float(input('Insira o valor da reta: '))
r3 = float(input('Insira o valor da reta: '))
if r1 + r2 >= r3 and r1 + r3 >= r2 and r3 + r2 >= r1:
    print('Forma um triângulo!') 
else:
    print('Não forma um triângulo!') 