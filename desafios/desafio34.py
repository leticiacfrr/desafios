print('Calculando o Aumento!')
sal = float(input('Qual o valor do seu salário? '))
if sal > 1250.00:
    aumento1 = sal * 0.1
    valor1 = sal * 1.1
    print('O seu aumento será de {:.2f} e seu novo salário será de {:.2f}'. format(aumento1, valor1))
else:
    aumento2 = sal * 0.15
    valor2 = sal * 1.15
    print('O seu aumento será de {:.2f} e seu novo salário será de {:.2f}'. format(aumento2, valor2))