cidade = input('Insira o nome da sua cidade (considerando letras maiúsculas): ')
cidade_separada = cidade.split()
termo = 'Santo'
if termo in cidade_separada[0]:
    print('Há "Santo" no início do nome da cidade')
elif ('santo' in cidade_separada[0]):
    print('Você esqueceu a letra maiúscula! Mas há "Santo no início do nome da cidade')
else:
    print('Não há "Santo" no início do nome da cidade')