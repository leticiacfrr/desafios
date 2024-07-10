print('Palíndromo')
frase = input('Escreva sua frase: ')
remover_espaços = ''.join(frase.split())
print(remover_espaços)
cont_caracteres = (len(remover_espaços))
q_l_igual = 0
print(cont_caracteres)
for l in range (0 , cont_caracteres // 2):
    if remover_espaços[l] == remover_espaços[cont_caracteres - l - 1]:
        q_l_igual = q_l_igual + 1
print(q_l_igual)
if q_l_igual == cont_caracteres // 2:
    print('A frase: "{}" é um palíndromo!'.format(frase))
else:
    print('A frase: "{}" não é um palíndromo!'.format(frase))