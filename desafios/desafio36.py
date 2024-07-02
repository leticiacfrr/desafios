print('EMPRÉSTIMO BANCÁRIO')
vcasa = float(input('Valor do imóvel: '))
salario = float(input('Valor do salário: '))
quant_anos = float(input('Quantidade de anos: '))
prestação = vcasa / quant_anos
if prestação <= salario * 0.3:
    print('Parabéns, você pode realizar o empréstimo! O valor da prestação é {}'.format(prestação))
else:
    print('Sinto muito, você não pode realizar o empréstimo!') 