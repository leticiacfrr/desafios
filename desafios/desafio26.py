frase = input('Insira um frase: ')
print('A letra "a" aparece {} vezes'.format(frase.lower().count('a')))
print('A letra "a" aparece a primeira vez na posição {}'.format(frase.lower().find('a')))
print('A letra "a" aparece a última vez na posição {}'.format(frase.lower().rfind('a')))