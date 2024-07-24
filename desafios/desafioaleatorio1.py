frase = ''.join(input('Digite uma frase: ').lower().split())
vogais = 'aeiou'
contador_vogais = 0
print(frase)
print(len(vogais))
print(len(frase))
for c in range(0, len(vogais)):
    if frase.__contains__(vogais [c]):
        contador_vogais += frase.count(vogais[c])
print('A quantidade de vogais são {} e de consoantes são {}'. format(contador_vogais, len(frase)- contador_vogais))

#while frase != 'pare':
    #frase = input('Digite uma frase: ').lower()
    #print(frase.count(vogais))
    