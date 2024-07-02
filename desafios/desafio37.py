n = int(input('Insira um número inteiro: '))
baseconversão = int(input('Escolha a base de conversão entre 1 e 3: '))
if baseconversão == 1:
    b = f'{n:08b}'
    print('Está é a representação binaria de {}: {}'.format(n, b))
elif baseconversão == 2:
    o = f'{n:04o}'
    print('Está é a representação octal de {}: {}'.format(n, o))
else:
    h = f'{n:04x}'
    print('Está é a representação hexadecimal de {}: {}'.format(n, h))