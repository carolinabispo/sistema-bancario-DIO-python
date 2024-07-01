import textwrap

def menu():
    return """
=========== BEM VINDO AO DIO-bank ============

    Selecione qual a opção deseja abaixo:

    [1] Depósitos
    [2] Saques
    [3] Extratos
    [4] Sair
"""

saldo = 0
saque_diarios = 3
limite = 500
numero_saques = 0
extrato = ""

def depositar_dinheiro(deposito):
    global saldo 
    if deposito > 0:
        saldo += deposito
        print(f"Esse é o valor do seu depósito: R${deposito:.2f}")
    else:
        print("Quantia inválida")
    print(f"Seu saldo atual: R${saldo:.2f}")

def sacar_dinheiro(saque):
    global saldo, extrato, numero_saques
    if numero_saques >= saque_diarios:
        print(f"Limite de saques diários atingidos, saldo atual: R${saldo:.2f}")
    elif saque > limite:
        print(f"O valor máximo a ser sacado é de R${limite:.2f}, por favor retorne ao menu de opções")
    elif saque > saldo:
        print(f"Saldo insuficiente para saque, seu saldo total é de R${saldo:.2f}")
    elif saque <= 0:
        print("Valor de saque inválido")
    else:
        saldo -= saque
        extrato += f"\nSaque: R${saque:.2f}"
        numero_saques += 1
        print(f"Saque de R${saque:.2f} realizado com sucesso!")
        print(f"Esse é seu saldo atual: R${saldo:.2f}")

def verificar_extrato():
    global extrato
    extrato_msg = extrato if extrato else "Não foram realizadas movimentações"
    mensagem_final = f"""
        =============== EXTRATO ===============
        {extrato_msg}
        Saldo atual: R${saldo:.2f}
        """
    print(mensagem_final)

def realizar_operacoes():
    while True:
        operacoes = input(menu())
        if operacoes == "1":
            deposito = float(input("Insira o valor a ser depositado: "))
            depositar_dinheiro(deposito=deposito)
        elif operacoes == "2":
            saque_valor = float(input("Insira o valor de saque: "))
            sacar_dinheiro(saque=saque_valor)
        elif operacoes == "3":
            verificar_extrato()
        elif operacoes == "4":
            print("Obrigado por usar nossos serviços")
            break
        else:
            print("Opção inválida")

clientes = []

def novo_cliente():
    cpf = input("Insira seu CPF: ")
    nome = input("Insira seu nome: ")
    data_nascimento = input("Insira sua data de nascimento: ")
    endereco = input("Insira seu endereço: ")

    cliente = {
        "CPF": cpf,
        "Nome": nome,
        "Data de nascimento": data_nascimento,
        "Endereço": endereco
    }
    
    for c in clientes:
        if c["CPF"] == cpf:
            return None  # CPF já cadastrado, retorna None
    
    clientes.append(cliente)
    return cpf  # Retorna o CPF do novo cliente

def autenticacao(cpf):
    for cliente in clientes:
        if cliente["CPF"] == cpf:
            return True
    return False

def acessar_nome(cpf):
    for cliente in clientes:
        if cliente["CPF"] == cpf:
            return cliente["Nome"]
    return None

def criar_conta(agencia, numero_conta, cpf):
    if autenticacao(cpf):
        nome_usuario = acessar_nome(cpf)
        if nome_usuario:
            print("\n=== Conta criada com sucesso! ===")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": nome_usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def cadastro():
    contas = []
    AGENCIA = "0001"
    while True:
        menu_cadastro = ("""
            =============================
                [1] Novo cliente
                [2] Já sou cadastrado   
                [3] Criar nova conta
                [4] Listar contas
                [0] Sair
            =============================
            """)
        
        opcao = int(input(menu_cadastro))
        if opcao == 0:
            print("Saiu do sistema.")
            break
        elif opcao == 1:
            cpf = novo_cliente()
            if cpf:
                print(f"Novo cliente cadastrado!")
            else:
                print("Cliente já cadastrado!")
        elif opcao == 2:
            cpf_login = input("Insira seu CPF: ")
            if autenticacao(cpf_login):
                print(f"Seja bem-vindo ao DIO-bank: {acessar_nome(cpf_login)}")
                realizar_operacoes()
            else:
                print("Cliente não encontrado")
        elif opcao == 3:
            cpf = input("Informe o CPF do usuário para criar a conta: ")
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, cpf)
            if conta:
                contas.append(conta)
        elif opcao == 4:
            listar_contas(contas)
        else:
            print("Opção inválida")

cadastro()
