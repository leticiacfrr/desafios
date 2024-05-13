nome = input('Escreva seu nome completo: ')
print(nome.upper())#tudo maisculo
print(nome.lower())#tudo minusculo
print(len(nome.replace(' ','')))
primeiro_nome = nome.split()
print(len(primeiro_nome[0]))
#print(len(nome.split()[0]))
