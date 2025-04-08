#disciplina: nome, codigo, duração e carga horaria
#aluno: nome, matricula, cpf e disciplina
#professor: nome, telefone, endereço, cpf, titulação, salário e area de pesquisa
#o programa deve dizer quais disciplinas são ministradas por cada professor e quais alunos estão matriculados em cada disciplina por meio de uma lista
#deve ter menu de registro para disciplina, aluno e professor 
class Disciplinas:
    def __init__(self):
        self.nome = ''
        self.codigo = '' 
        self.duracao = ''
        self.cargahoraria = ''

class Aluno:
    def __init__(self):
        self.nome = ''
        self.matricula = ''
        self.cpf = ''
        self.disciplina = ''

class Professor:
    def __init__(self):
        self.nome = ''
        self.telefone = ''
        self.endereço = ''
        self.cpf = ''
        self.titulacao = ''
        self.areapesquisa = ''
        self.salario = ''

def cadastrar_disciplina():
    print('CADASTRO DE DISCIPLINAS \nInsira os dados corretamente \n')
    nome = (input('Nome: '))
    codigo = (input('Código: '))
    duracao = (input('Duração: '))
    cargahoraria = (input('Carga horária: '))

def cadastrar_aluno():
    print('CADASTRO DE ALUNOS \nInsira os dados corretamente \n')
    nome = (input('Nome: '))
    matricula = (input('Matrícula '))
    cpf = (input('CPF: (Por favor, insira-o sem a utilização de símbolos. ex.: 00000000000) '))
    disciplina = (input('Codigo: '))

def cadastrar_professor():
    print('CADASTRO DE PROFESSORES \nInsira os dados corretamente \n')
    nome = (input('Nome: '))
    telefone = (input('Número: '))
    endereço = (input('Endereço: '))
    cpf = (input('CPF: (Por favor, insira-o sem a utilização de símbolos. ex.: 00000000000)'))
    titulacao = (input('Titulação: '))
    areapesquisa = (input('Área de pesquisa: '))
    salario = (input('Salário: '))

def menu():
    while True:
        print('ESCOLHA A OPÇÃO DESEJADA \n')
        print('1- Cadastrar disciplina')
        print('2- Cadastrar aluno')
        print('3- Cadastrar professor')
        print('4- Lista de disciplinas')
        print('5- Lista de professores')
        print('6- Finalizar programa \n')
        opção = (input('Qual a opção? '))
        if opção == '1':
            cadastrar_disciplina()
        elif opção == '2':
            cadastrar_aluno()
        elif opção == '3':
            cadastrar_professor()
        elif opção == '4':
            listadedisciplinas
        elif opção == '5':
            listadeprofessores
        else:
            print('\nObrigada, adeus!')
            break