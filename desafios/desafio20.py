from random import shuffle
print('Sorteio de alunos')
a1 = str(input('Insira o nome do aluno: '))
a2 = str(input('Insira o nome do aluno: '))
a3 = str(input('Insira o nome do aluno: '))
a4 = str(input('Insira o nome do aluno: '))
lista = [a1,a2,a3,a4]
shuffle(lista)
print('O aluno é: {}'.format(lista))