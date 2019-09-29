lista_aluno = []
nota_aluno = []
falta_aluno = []
registro_aluno = []
def menu():
    print('1 Matricula do aluno:')
    print('2 Remover matricula:')
    print('3 Lançar nota:')
    print('4 Lançar falta:')
    print('5 Situação do aluno:')
    print('6 Sair:')
    opcao=int(input('Digite sua Opção:'))
    return opcao


def matricula():
    nome=str(input('Digite o nome completo do aluno:'))
    rg=str(input('Digite o RG do aluno:'))
    if len(rg)>9 or len(rg)<9:
        print("RG inexistente!")
        rg=str(input('Digite novamente o rg:'))

    cpf=str(input('Digite o CPF do aluno:'))
    if len(cpf)>11 or len(cpf)<11:
        print("CPF inexistente!")
        cpf=str(input('Digite novamente o cpf:'))

    endereco=str(input('Digite o endereço do aluno:'))
    lis = ["Nome:",nome,"Rg:",rg,"CPF",cpf,"Endereço:",endereco]
    lista_aluno.append(lis)
    print('Cadastro do aluno feito:')

def Remover():
    nome=str(input('Digite o nome do aluno:'))
    for i in lista_aluno:
        if i[1]==nome:
            del(lista_aluno[:1])
            print("O aluno",nome,"foi removido do sistema")
        else:
            print("Esse aluno nao existe")
            nome=str(input('Digite novamente o nome do aluno:'))
            print("Aluno removido!")
    

def nota():
    nome=str(input('Digite o nome do aluno:'))
    for i in lista_aluno:
        if i[1]==nome:
            n1=float(input('Digite a primeira nota:'))
            n2=float(input('Digite a segunda nota:'))
            n3=float(input('Digite terceira nota:'))
            media=float((n1+n2+n3)/3)
            nota_aluno.append([nome,media])
            print("A nota do aluno",nome,"está no sistema")
        else:
            print("Esse aluno nao existe ")


def falta():
    nome=str(input('Digite o nome do aluno:'))
    for i in lista_aluno:
        if i[1]!=nome:
            print('Esse aluno nao existe!')
        elif i[1]==nome:
            horas=float(input("digite a quantidade de falta do aluno(em horas):"))
            falta_aluno.append([nome,horas])
            print("Nota lançada no sistema")
    


def situacao():
    nome=str(input('Digite o nome do aluno:'))
    for i in lista_aluno:
        for j in nota_aluno:
            for k in falta_aluno:
                if i[1]==nome and j[0]==nome and k[0]==nome:
                    print('A media do aluno',i[1],'é',j[1])
                    print('A quantidade de falta do aluno é',k[1],('horas'))

