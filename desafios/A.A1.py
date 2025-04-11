#disciplina: nome, codigo, duração e carga horaria
#aluno: nome, matricula, cpf e disciplina
#professor: nome, telefone, endereço, cpf, titulação, salário e area de pesquisa
#o programa deve dizer quais disciplinas são ministradas por cada professor e quais alunos estão matriculados em cada disciplina por meio de uma lista
#deve ter menu de registro para disciplina, aluno e professor 

# criação do objeto Disciplina com suas atribuições
class Disciplina:
    def __init__(self, nome, codigo, duração, carga_horaria):
        self.nome = nome
        self.codigo = codigo
        self.duração = duração
        self.carga_horaria = carga_horaria
        self.professor = None
        self.alunos = []

# criação do objeto Aluno com sua atribuições
class Aluno:
    def __init__(self, nome, matricula, cpf):
        self.nome = nome
        self.matricula = matricula
        self.cpf = cpf
        self.disciplinas = []

#criação do objeto Professor com suas atribuições
class Professor:
    def __init__(self, nome, telefone, endereço, cpf, titulação, area_pesquisa, salario):
        self.nome = nome
        self.telefone = telefone
        self.endereço = endereço
        self.cpf = cpf
        self.titulação = titulação
        self.area_pesquisa = area_pesquisa
        self.salario = salario
        self.disciplinas = []

#armazenando dados
disciplinas = []
alunos = []
professores = []

#função cadastro de disciplinas
def cadastrar_disciplina():
    print('CADASTRO DE DISCIPLINAS \nInsira os dados corretamente \n')
    nome = (input('Nome: '))
    codigo = (input('Código: '))
    duração = (input('Duração: '))
    carga_horaria = (input('Carga horária: '))

    disciplina = Disciplina(nome, codigo, duração,carga_horaria)

    # escolha do professor com mostrador de professores cadastrados
    print("\nProfessores disponíveis:")
    for i, prof in enumerate(professores, 1):
        print(f"{i} - {prof.nome}")
    escolha = int(input("Digite o número do professor para essa disciplina: "))

    # Verifica se a escolha é válida e cadastro de disciplina
    if 1 <= escolha <= len(professores):
        professor = professores[escolha - 1]
        disciplina.professor = professor
        professor.disciplinas.append(disciplina)
        disciplinas.append(disciplina)
        print("Disciplina cadastrada com sucesso!\n")
    else:
        print("Número inválido. A disciplina não foi cadastrada.\n")

# função cadastro de alunos
def cadastrar_aluno():
    print('CADASTRO DE ALUNOS \nInsira os dados corretamente \n')
    nome = (input('Nome: '))
    matricula = (input('Matrícula: '))
    cpf = (input('CPF: (Por favor, insira-o sem a utilização de símbolos. ex.: 00000000000) '))

    aluno = Aluno(nome, matricula, cpf)
    
    # escolha da disciplina com mostrador de displinas cadastradas
    print("\nEscolha as disciplinas para esse aluno (digite os códigos separados por vírgula):")
    for i, disc in enumerate(disciplinas):
        print(f"{disc.codigo} - {disc.nome}")
    codigos = input("Códigos das disciplinas: ").split(',')

    #procura a disciplina e adição do aluno a displina
    for cod in codigos:
        cod = cod.strip()
        for disc in disciplinas:
            if disc.codigo == cod:
                aluno.disciplinas.append(disc)
                disc.alunos.append(aluno)
                break
    
    #finalização do cadastro do aluno
    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!\n")

# função cadastro de professores
def cadastrar_professor():
    print('CADASTRO DE PROFESSORES \nInsira os dados corretamente \n')
    nome = (input('Nome: '))
    telefone = (input('Telefone: '))
    endereço = (input('Endereço: '))
    cpf = (input('CPF: (Por favor, insira-o sem a utilização de símbolos. ex.: 00000000000)'))
    titulacao = (input('Titulação: '))
    areapesquisa = (input('Área de pesquisa: '))
    salario = (input('Salário: '))

    #cadastro do professor
    professor = Professor(nome, telefone, endereço, cpf, titulacao, areapesquisa, salario)
    professores.append(professor)
    print("Professor cadastrado com sucesso!\n")

# função lista de disciplinas cadastradas
def listar_disciplinas():
    print('\nLISTA DE DISCIPLINAS:')

    # Percorre todas as disciplinas cadastradas mostrando seu dados
    for disc in disciplinas:
        print(f'\nDisciplina: {disc.nome} ({disc.codigo})')
        print(f'Duração: {disc.duracao}, Carga Horária: {disc.carga_horaria}')
        print(f'Professor: {disc.professor.nome if disc.professor else "Não atribuído"}')
        print('\nAlunos matriculados:')
        if disc.alunos:
            for aluno in disc.alunos:
                print(f' - {aluno.nome} (Matrícula: {aluno.matricula})')
        else:
            print(' - Nenhum aluno matriculado.')

# função lista de professores cadastrados
def listar_professores():
    print('\nLISTA DE PROFESSORES:')

    # Percorre todos os professores cadastrados e mostra seus dados
    for prof in professores:
        print(f'\nNome: {prof.nome}')
        print(f'Titulação: {prof.titulacao}, Área de Pesquisa: {prof.areapesquisa}')
        print(f'Disciplinas Ministradas:')
        if prof.disciplinas:
            for disc in prof.disciplinas:
                print(f' - {disc.nome} ({disc.codigo})')
        else:
            print(' - Nenhuma disciplina atribuída.')

# função menu de escolha de ação
def menu():
    while True:
        print('ESCOLHA A OPÇÃO DESEJADA \n')
        print('1- Cadastrar professor')
        print('2- Cadastrar disciplina')
        print('3- Cadastrar aluno')
        print('4- Lista de disciplinas')
        print('5- Lista de professores')
        print('6- Finalizar programa \n')
        opção = (input('Qual a opção? '))
        if opção == '1':
            cadastrar_professor()
        elif opção == '2':
            cadastrar_disciplina()
        elif opção == '3':
            cadastrar_aluno()
        elif opção == '4':
            listar_disciplinas()
        elif opção == '5':
            listar_professores()
        else:
            print('\nObrigada, adeus!')
            break

menu()