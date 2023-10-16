import csv
import os
from os import system
import time

##########################################################
# ORGANIZANDO A AGENDA
agenda = 'quest2/agendas/agenda.csv'
criado = False

### CRIA UMA PASTA AGENDAS CASO NAO EXISTE UMA
# (REMOVA O DIRETORIO QUEST2 DE TUDO SE QUISER QUE A PASTA SEJA CRIADA POR FORA)
if not os.path.exists('quest2/agendas'):
    os.makedirs('quest2/agendas')


if os.path.exists('quest2/agendas/agenda.csv'):
    criado = True

else:
    agenda = os.path.join("quest2/agendas", "agenda.csv")
# cria o agenda.csv na pasta agendas


while criado == False:
    dados = [
        ["Nome", "Numero"]

    ]

    with open(agenda, mode="w", newline="") as agenda_csv:
        adicionar_csv = csv.writer(agenda_csv)
        adicionar_csv.writerow(dados)

    criado = True


contatos = []

##########################################################
#CONFIGURANDO DEF's IMPORTANTES

def confirm_Numero(check):
    return check.isdigit()

##########################################################
# POSSIBILIDADES DA LISTA
lista = ['1', 'lista', 'listar', 'listagem', 'listar contatos', 'listar contato']
consulta = ['2', 'consulta', 'consultar', 'consultar contatos', 'consultar contato', 'buscar', 'busque', 'buscar contato', 'busque contato']
adicionar = ['3', 'adiciona', 'adicionar', 'add', 'adicionar contato', 'adicionar contatos', 'novo']
remover = ['4', 'remover', 'remova', 'remove', 'remover contato', 'remover contatos']

###########################################################
sair = False

while(sair == False):
    print("Bem vindo à sua agenda virtual.\nIndique o que deseja fazer:")
    print("Listar contatos\nConsultar contato\nAdicionar contato\nRemover contato\nSair")
    selector = input('\n')
    usefulSelec = selector.lower()


    if usefulSelec in lista:
        system('cls')
        def listar_contatos():
            nomes_contatos = []
            with open (agenda, mode='r') as agenda_csv:
                ler_csv = csv.reader(agenda_csv)
                ###ignorar a linha inicial dos coiso
                next(ler_csv, None)

                for linha in ler_csv:
                    nomes_contatos.append(linha[0])

                return nomes_contatos
            

        nomes_contatos = listar_contatos()

        if nomes_contatos:
            print("Nomes dos contatos: ")
            for nome in nomes_contatos:
                print(nome)

            print("\n")
            time.sleep(2)

        else:
            system('cls')
            print('A lista está vazia.\n\n')
            time.sleep(2)


    elif usefulSelec in consulta:
        system('cls')

        def buscar_contato(nome_contato):
            with open(agenda, mode='r') as agenda_csv:
                ler_csv = csv.reader(agenda_csv)
                #### Pular a linha do nome dos coiso (linha inicial)
                next(ler_csv, None)

                for linha in ler_csv:
                    if linha[0].lower() == nome_contato.lower():
                        return {"Nome": linha[0], "Número": linha[1]}
                
            return None
            ### Se não achar o nome não vai retornar NADAAA

        system('cls')
        contato_nome = input("Digite o nome do contato que deseja procurar: ")
        achar_contato = buscar_contato(contato_nome)

        if achar_contato:
            system('cls')
            print(f"\nNome do contato: {achar_contato['Nome']}\nNúmero do contato: {achar_contato['Número']}\n")
            time.sleep(2)

        else:
            system('cls')
            print(f"O contato '{contato_nome}' não foi encontrado. Tente novamente.\n\n")
            time.sleep(2)


    elif usefulSelec in adicionar:
        adicionado = False
        system('cls')
        print("Informe o nome do contato: ")
        nome = input()

        ### WHILE PARA CHECAR SE O INPUT É NUMÉRICO E PERMITIR A PASSAGEM
        while not adicionado:
            print("Informe o número do contato: ")
            numero = input()
            if confirm_Numero(numero):
                adicionado = True
            else:
                print("\nO número foi inserido incorretamente, verifique e tente novamente!\n")

        # Abre o arquivo CSV no modo de escrita (modo "a" para adicionar)
        with open(agenda, mode="a", newline="") as agenda_csv:
            adicionar_csv = csv.writer(agenda_csv)
            adicionar_csv.writerow([nome, numero])  # Adiciona apenas o novo contato ao arquivo

        print("\nContato adicionado com sucesso.")
        time.sleep(2)
        system('cls')


    elif usefulSelec in remover:
        #################################################
        # FUNCAO PARA REMOVER O NOME DE UM CONTATO
        system('cls')
        def remover_contato(nome_contato):

            with open(agenda, mode='r') as agenda_csv:
                ler_csv = csv.reader(agenda_csv)
                contatos_info = list(ler_csv)
            
            encontrado = False
            for linha in contatos_info:
                if linha[0].lower() == nome_contato.lower():
                    nomeOrig = linha[0]
                    contatos_info.remove(linha)
                    encontrado = True
                    break
         ###############################################
            
            # ATUALIZANDO A AGENDA PARA A LISTA SEM A LINHA
            if encontrado:
                with open(agenda, mode='w', newline='') as agenda_csv:
                    atualizar_csv = csv.writer(agenda_csv)
                    atualizar_csv.writerows(contatos_info)

                system('cls')
                print(f"O contato '{nomeOrig}' foi removido com sucesso!")
                time.sleep(2)
                system('cls')
            
            else:
                system('cls')
                print(f"O contato '{nome_contato}' não existe.")
                time.sleep(2)

        contato_remover = input("Digite o nome do contato que deseja remover: ")
        remover_contato(contato_remover)


    elif usefulSelec == 'sair':
        sair = True


    else:
        print("\nOpção não encontrada. tente novamente.\n")
        time.sleep(2)
