int #inteiros: 1, 2, -3
float #reais ou flutuantes: 4.5, 0.790, -15.74
bool #booleanos ou logicos: True, False (sempre a primeira letra maiuscula)
str # caracteres ou strings: 'ola', '7.5', ''
type #mostra o tipo da variavel
n1 = int(input('valor: '))
n2 = int(input('valor: '))
s = n1 + n2
#print ('a soma entre', n1, 'e', n2, 'é:',s)
print ('a soma entre {} e {} vale {}'.format(n1, n2, s)) #novo formato de print