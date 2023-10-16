import os
saldo = 0 
fim = False

consulta = ['1', 'consulta', 'consultar', 'consultar saldo', 'consulta de saldo']
depositar = ['2', 'deposito', 'depositar', 'depositar dinheiro']
sacar = ['3', 'saque', 'sacar', 'sacar dinheiro']
sair = ['4', 'sair', 'encerrar', 'end', 'quit']

while fim == False:
    print("Bem-vindo ao simulador de caixa!")
    print("Escolha uma das opções")
    escolha = input("1. Consultar saldo\n2. Depositar\n3. Sacar\n4.Sair\n")
    
    if escolha.lower() in consulta:
        os.system('cls')
        print("O seu saldo é de R$" + str(saldo) + "\n")
        
    elif escolha.lower() in depositar:
        os.system('cls')
        deposito = input("Insira a quantia que deseja depositar: ")
        
        if deposito.isdigit() and int(deposito) >= 0:
            saldo = saldo + int(deposito)
            print("\nValor depositado com sucesso!")
            
        else: print("Valor incorreto! Verifique o valor depositado e tente novamente.")
        
    elif escolha.lower() in sacar:
        os.system('cls')
        saque = input("Insira a quantia que deseja sacar: ")
        
        if saque.isdigit() and int(saque) <= saldo:
            saldo = saldo - int(saque)
            print("\nValor sacado com sucesso!\n")
            
        elif saque.isdigit() and int(saque) > saldo:
            print("\nO valor na conta é insuficiente\n")
            
        else:
            print("Valor incorreto! Verifique o valor depositado e tente novamente.\n")
            
    elif escolha.lower() in sair:
        fim = True
        
    else:
        print('\nOpçao incorreta, Verifique o valor e tente novamente.\n')