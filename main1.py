import FuncoesCd2 as f
opcao = 0
while opcao!= 6:

    opcao = f.menu()

    if opcao == 1:
        f.matricula()
    elif opcao == 2:
        f.Remover()
    elif opcao == 3:
        f.nota()
    elif opcao == 4:
        f.falta()
    elif opcao == 5:
        f.situacao()
    elif opcao == 6:
        print("Saindo do sistema")
    else:
        print('Opcao não existente')
        opcao = 0


        
        
    




   