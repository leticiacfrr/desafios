frase = 'curso em video python' #cada caractere da string ocupa um micro espaço, numerico, na memoria. vai de 0 até n.

#fatiamento (a frase possui 21 caracteres, de 0 a 20)
print(frase[9]) #acessando a posição 9 da string
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

#divisão
print(frase.split())#gera uma lista com todas as palavras em uma cadeia de caracteres. uma lista onde cada palavra/elemento é separada pelo seu split
#''.join(frase.split()) elimina os espaços e junta tudo em uma string só

#junção
print(''.join(frase.split()))#junta a frase sem espaços

#como printar um texto maior
print('''Python é popular devido à sua sintaxe limpa, vasta biblioteca de recursos, 
multiplataforma e comunidade ativa. É eficiente, acessível e versátil, 
sendo uma excelente escolha para uma ampla gama de projetos de desenvolvimento de software.''')
