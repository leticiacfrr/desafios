nota1 = float(input('Insira a nota: '))
nota2 = float(input('Insira a nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Reprovado!')
elif 5.0 < media < 6.9:
    print('Recuperação!')
else:
    print('Aprovado!')