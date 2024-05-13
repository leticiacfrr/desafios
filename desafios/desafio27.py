nome = input('Escreva seu nome completo: ')
nome_separado = nome.split()
print(len(nome_separado))
print('''Nome: {}
      Primeiro nome: {} 
      Ultimo nome: {}'''.format(nome, nome_separado[0],nome_separado[len(nome_separado) - 1]))
