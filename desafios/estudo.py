# valor = 5 + 3
# if valor == 7:
#     print("é igual")
# else:
#     print('não é igual')
#ordem de precedência de operadores
#()
#**
#* / // %
# + - 
n1 = int(input('insira um valor: ')) # o :.3f é para as casas decimais a serem consideradas
n2 = int(input('insira um valor: ')) # o \n seguinifica quebra de linha
s = n1 + n2                          # o end=' ' significa ñ quebra de linha
m = n1 * n2
d = n1 /n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, o produto é {}, a divisão é {:.3f}, a divisão inteira é {} e a potência é {}'.format(s, m, d, di,e))
