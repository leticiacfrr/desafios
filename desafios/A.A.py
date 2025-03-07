print('CRIANDO UMA LISTA!')
dados = (input('Primeiro, insira aqui os elementos da sua lista (permitidos apenas números inteiros): '))
lista = dados.strip()
lista = dados.split(',')

def a():
    novo_num = (input('\nInsira aqui o novo número: '))
    lista.append(novo_num)
    print('{} adicionado com sucesso.\n'.format(novo_num))
def b():
    num = (input('Insira o número que procura: '))
    if num in lista:
        print('{} está na lista!\n'.format(num))
    else:
        print('{} não está na lista!\n'.format(num))
def c():
    lista_crescente = sorted(lista, key=int)
    print('{} \n'.format(lista_crescente))
def d():
    lista_decrescente = sorted(lista, reverse=True, key=int)
    print('{} \n'.format(lista_decrescente))

def menu():
    while True:
        print('\nAgora escolha uma opção: \n')
        print('a (Adicionar mais um número)')
        print('b (Procurar um número da lista)')
        print('c (Exibir a lista em ordem crescente)')
        print('d (Exibir a lista em ordem decrescente)')
        print('e (Encerrar o programa) \n')
        opção = (input('a, b, c ,d ou e: '))
        if opção == 'a':
            a()
        elif opção == 'b':
            b()
        elif opção == 'c':
            c()
        elif opção == 'd':
            d()
        else:
            print('\nPrograma encerrado, obrigada!')
            break  
menu()