opção1 = "1 - Cadastrar novo usuário"
opção2 = "2 - Lista usuários"
opção3 = "3 - Sair do sistema"
opção4 = "4 - Buscar usuário pelo nome"
opção5 = "5 - Remover usuário"
escolha = 0
CadastroUsuario = 0
Usuarios = list()
Idade = list()
separador = list()
nomepesquisa = ""
remover = ""

while escolha != 3:
    print("Opções:")
    print(opção1)
    print(opção2)
    print(opção3)
    print(opção4)
    print(opção5)
    
    escolha = int(input("Qual opção deseja fazer? "))
    print(escolha)
    
    if escolha == 1:
        CadastroUsuario = int(input("Deseja cadastrar quantas pessoas? "))
        if CadastroUsuario <= 0:
            print('Opção Inválida')
        else:
            for c in range(1, CadastroUsuario + 1):
                Usuarios.append(input(f"Digite o nome do {c}º usuário: "))
                Idade.append(input(f"Digite a idade do {c}º usuário: "))
                print(f"FIM DE CADASTRO DO USUÁRIO {c}!")
    
    elif escolha == 2:
        if len(Usuarios) > 0:
            print(f'Os usuários são: {Usuarios}')
            print(f'As idades são: {Idade}')
        else:
            print("Não temos nenhum usuário cadastrado.")
    
    elif escolha == 3:
        print("Encerrando programa.")
    
    elif escolha == 4:
        nomepesquisa = str(input("Qual nome deseja procurar? ")).strip()
        if nomepesquisa in Usuarios:
            print(f'O nome {nomepesquisa} foi encontrado.')
        else:
            print('Nome não encontrado.')
    
    elif escolha == 5:
        remover = str(input('Qual nome você gostaria de remover? ')).strip()
        if remover in Usuarios:
            index = Usuarios.index(remover)
            Usuarios.pop(index)
            Idade.pop(index)
            print(f'O nome {remover} foi removido com sucesso.')
        else:
            print('O usuário não está cadastrado.')
    
    else:
        print("Opção inválida. Tente novamente.")
