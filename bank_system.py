import locale
menu = """
=========== BEM VINDO AO DIO-bank ============

    Selecione qual a opção deseja abaixo:

    [1] Depósitos
    [2] Saques
    [3] Extratos
    [4] Sair
"""
saldo = 0
SAQUES_DIARIOS = 3
limite = 500
numero_saques = 0
extrato = ""



while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Insira o valor a ser depositado: ",))
        saldo += deposito
        # saldo += deposito
        print(f"Esse é seu saldo atual: R${saldo:.2f}")


    elif opcao == "2":
        saque = float(input("Insira o valor a ser sacado: "))
        
        # saldo -= saque
        
        if numero_saques >= SAQUES_DIARIOS:
                print("Limite de saques diários atingidos")
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

    elif opcao == "3":
        extrato_msg = extrato if extrato else "Não foram realizadas movimentações"

        mensagem_final = f"""
        =============== EXTRATO ===============
        {extrato_msg}
        Saldo atual: {saldo:.2f}

        """
        print(mensagem_final)

    elif opcao == "4":
        """ 
        ===========================================

            Obrigado por usar nosso sistema
            
        ===========================================
        """
        break

    else:
        print("insira uma opção existente")