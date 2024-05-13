frase = 'curso em video python' #cada caractere da string ocupa um micro espaço, numerico, na memoria. vai de 0 até n.

#fatiamento (a frase possui 21 caracteres, de 0 a 20)
print(frase[9])
print(frase[9:21])#matematicamente para explicar como funciona o fatiamento entre dois pontos seria [9:21[
print(frase[9:21:2])
print(frase[:5])#espaço vazio antes ou depois dos ":" significa ir do inicio ou do final
print(len(frase))#contagem de carateres da frase
print(frase.count('o'))#contagem de caractere individual
print(frase.find('deo'))#origem do caractere

#transformação
print(frase.replace('python','android'))#substituição
print(frase.upper())#tudo maisculo
print(frase.lower())#tudo minusculo
print(frase.capitalize())
print(frase.title())
#frase1 = '   Aprenda Python  '
#print(frase1.strip())#remove espaços desnecessários, se colocar um 'r'antes do strip elimina só os espaços da direita. se colocar um 'l', elimina os da esquerda.

#divisão
print(frase.split())#gera uma lista com todas as palavras em uma cadeia de caracteres. uma lista onde cada palavra/elemento é separada pelo seu split

#junção
print(''.join(frase))#junta a frase

#como printar um texto maior
print('''Python é popular devido à sua sintaxe limpa, vasta biblioteca de recursos, 
multiplataforma e comunidade ativa. É eficiente, acessível e versátil, 
sendo uma excelente escolha para uma ampla gama de projetos de desenvolvimento de software.''')
