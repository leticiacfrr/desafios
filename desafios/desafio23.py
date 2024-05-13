numero = int(input('Insira um número de 0 a 9999: '))
if (0 <= numero and numero <= 9999):
    numero_str = str(numero)
    if (len(numero_str) == 3):
        numero_str = '0' + numero_str
    elif (len(numero_str) == 2):
        numero_str = '00' + numero_str
    elif (len(numero_str) == 1):
        numero_str = '000' + numero_str
    print('milhar: {} centena: {} dezena: {} unidade: {}'.format(numero_str[0], numero_str[1], numero_str[2], numero_str[3]))
else:
    print('Não aceito este numero!')