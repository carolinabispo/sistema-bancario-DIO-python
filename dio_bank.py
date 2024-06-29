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
   
    if (deposito > 0):
        saldo += deposito
        print(f"Esse é o valor do seu depósito: R${deposito:.2f}")
    else:
        print("Quantia invalida")

    return print(f"Seu saldo atual: R${saldo:.2f}")

# -----------------------------------------------------------------------------------------------
    
def sacar_dinheiro (saque):
    global saldo, extrato, numero_saques
 

    if numero_saques >= saque_diarios:
                print(f"Limite de saques diários atingidos, saldo atual: {saldo:.2f}")
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

    return saldo, extrato

def verificar_extrato():
    global extrato
    extrato_msg = extrato if extrato else print("Não foram realizadas movimentações")

    mensagem_final = f"""
        =============== EXTRATO ===============
        {extrato_msg}
        Saldo atual: {saldo:.2f}

        """
    return print(mensagem_final)


def realizar_operacoes():
    while True:
        operacoes = input(menu())

        if operacoes == "1":
            deposito = float(input("Insira o valor a ser depositado: "))
            depositar_dinheiro(deposito=deposito)
            
        elif operacoes == "2":
            # extrato = ""
            saque_valor=float(input("Insira o valor de saque: "))
            sacar_dinheiro(saque=saque_valor)
        elif operacoes == "3":
            verificar_extrato()
        elif operacoes == "4":
            print("Obrigado por usar nossos serviços")
            (cadastro())
            break
        else:
            print("Opção inválida")

# realizar_operacoes()


clientes = []
def novo_cliente():
    
    cpf = str(input("Insira seu CPF: "))
    nome = str(input("Insira seu nome: "))
    data_nascimento = str(input("Insira sua data de nascimento: "))
    endereco = str(input("Insira seu endereço: "))

    clientes_dict = {
        "CPF": cpf,
        "Nome": nome,
        "Data de nascimento": data_nascimento,
        "Endereço": endereco
    }
    
    cpf = clientes_dict["CPF"]
    lista_clientes = [cliente["CPF"] for cliente in clientes]

    if cpf in lista_clientes:
          return False
    else: 
        clientes.append(clientes_dict)
        return True

# acessar_cliente = novo_cliente()
def autentificacao(cpf):
     for cliente in clientes:
        if cliente["CPF"] == cpf:
            return True
        else: 
             return None
        
def acessar_nome(cpf):
     for cliente in clientes:
        if cliente["CPF"] == cpf:
            return cliente["Nome"]


def cadastro():
    while True:
        menu_cadastro = ("""
            =============================

                [1] Casdastrar novo cliente
                [2] Já sou cadastrado   
                [0] Sair
                        
            =============================
            """)
        

        opcao = int(input(menu_cadastro))
        
        if opcao == 0:
            print("saiu")
            break
        elif opcao == 1:
            cadastro = novo_cliente()
            if cadastro:
                print(f"Novo cliente cadastrado!")
            else:
                print("Cliente já cadastrado!")
        elif opcao ==2:
            cpf_login = input("Insira seu CPF: ")
            
            if autentificacao(cpf_login):
                print(f"Seja bem vindo ao DIO-bank: {acessar_nome(cpf_login)}")
                realizar_operacoes()
            else:
             print("Cliente não encontrado")
        else:
            print("Opção inválida")

cadastro()










    






# while True:
#     opcao = input(menu())







#  while True:
#     opcao = input(menu)

#     if opcao == "1":
#         deposito = float(input("Insira o valor a ser depositado: ",))
#         saldo += deposito
#         # saldo += deposito
#         print(f"Esse é seu saldo atual: R${saldo:.2f}")


#     elif opcao == "2":
#         saque = float(input("Insira o valor a ser sacado: "))
        
#         # saldo -= saque
        
#         if numero_saques >= SAQUES_DIARIOS:
#                 print("Limite de saques diários atingidos")
#         elif saque > limite:
#                 print(f"O valor máximo a ser sacado é de R${limite:.2f}, por favor retorne ao menu de opções")
#         elif saque > saldo:
#                 print(f"Saldo insuficiente para saque, seu saldo total é de R${saldo:.2f}")
#         elif saque <= 0:
#              print("Valor de saque inválido")
#         else:
#             saldo -= saque
#             extrato += f"\nSaque: R${saque:.2f}"
#             numero_saques += 1
#             print(f"Saque de R${saque:.2f} realizado com sucesso!")
#             print(f"Esse é seu saldo atual: R${saldo:.2f}")

#     elif opcao == "3":
#         extrato_msg = extrato if extrato else "Não foram realizadas movimentações"

#         mensagem_final = f"""
#         =============== EXTRATO ===============
#         {extrato_msg}
#         Saldo atual: {saldo:.2f}

#         """
#         print(mensagem_final)

#     elif opcao == "4":
#         print(""" 
#         ===========================================

#             Obrigado por usar nosso sistema
            
#         ===========================================
#         """)
#         break

#     else:
#         print("insira uma opção existente")