import json
import os
import time

todo = 'todo/todo.json'
with open(todo, mode='r') as todo_json:
    ler_json = json.load(todo_json)


verTask = ['1', 'ver', 'visualizar', 'conferir', 'observar', 'ver tarefa', 'ver tarefas']
adicionarTask = ['2', 'add', 'adicionar', 'adicione', 'adicionar tarefa', 'adicionar tarefas']
concluirTask = ['3', 'concluir', 'concluido', 'concluir tarefa', 'concluir tarefas']
removerTask = ['4', 'remover', 'remove', 'remova', 'remover tarefa', 'remover tarefas']
encerrar = ['5', 'sair', 'quit', 'encerrar', 'encerra', 'encerre']
escolha = ''

while not escolha in encerrar:
    print("Bem-vindo ao gerenciador de tarefas!\nO que desejar fazer?")
    escolha = (input("\n1. Ver tarefas\n2. Adicionar tarefa\n3. Concluir tarefa\n4. Remover tarefa\n5. Encerrar\n")).lower()

    if escolha in verTask:
        os.system('cls')

        for linha in ler_json['tarefas']:
            for pendencia, nomeTask in linha.items():
                print(f"{pendencia}: {nomeTask}\n")

        if len(ler_json['tarefas']) == 0: 
            print('\nA lista está vazia!\n')
            time.sleep(2)
        
        else: time.sleep(2)


    elif escolha in adicionarTask:
        os.system('cls')
        adicionar = input("Insira o nome da nova tarefa: ")
        existe = 0

        for linha in ler_json['tarefas']:
            for sentenca, nomeTask in linha.items():
                if nomeTask.lower() == adicionar.lower():
                    print("\nTarefa já existe na lista!\n")
                    existe = 1
                    time.sleep(2)

        if existe != 1:
            addTask = {"PENDENTE": adicionar}
            ler_json["tarefas"].append(addTask) 
            with open(todo, mode='w') as todo_json:
                json.dump(ler_json, todo_json, indent=2) ###Indent para quebra de linha e recuo

            print("\nTarefa inserida com sucesso!\n")
            time.sleep(2)


    elif escolha in concluirTask:
        os.system('cls')
        if len(ler_json['tarefas']) == 0: 
            print('\nA lista está vazia!\n')
            time.sleep(2)

        else:
            tarefa = input("Insira a tarefa que deseja concluir (posição ou nome): ")


            if tarefa.isdigit():
                quantLinhas = 0
                for linha in ler_json['tarefas']:
                    quantLinhas += 1
                
                if int(tarefa) > quantLinhas or int(tarefa) <= 0:
                    print('\nLinha não existe!\n')
                    time.sleep(2)
                
                else:
                    for sentenca, nomeTask in ler_json['tarefas'][int(tarefa) - 1].items():
                        if sentenca == "CONCLUIDO":
                            print("\nEsta tarefa já está concluída!\n")
                            time.sleep(2)

                        else:
                            sentenca = "CONCLUIDO"
                            ler_json['tarefas'][int(tarefa) - 1] = {sentenca: nomeTask}

                            with open(todo, mode='w') as todo_json:
                                json.dump(ler_json, todo_json, indent=2)
                                print("\nTarefa concluída com sucesso!\n")
                                time.sleep(2)

            else:
                for linha in ler_json['tarefas']:
                    for ignorar, nomeTask in linha.items():
                        if tarefa.lower() == nomeTask:
                            encontrado = 1
            
            
                if encontrado != 0:
                    for index, linha in enumerate(ler_json['tarefas']): ### enumerate retorna tanto o index quanto o valor da saída
                        for sentenca, nomeTask in linha.items():
                            if tarefa.lower() == nomeTask.lower():
                                if sentenca == "CONCLUIDO":
                                    print("\nEsta tarefa já está concluída!\n")
                                    time.sleep(2)

                                else:
                                    sentenca = "CONCLUIDO"
                                    ler_json['tarefas'][index] = {sentenca: nomeTask}

                                    with open(todo, mode='w') as todo_json:
                                        json.dump(ler_json, todo_json, indent=2) ###Indent para quebra de linha e recuo

                                    print("\nTarefa concluída com sucesso!\n")
                                    time.sleep(2)
                
                else: 
                    print("\nTarefa não existe!\n") 
                    time.sleep(2) 


    elif escolha in removerTask:
        os.system('cls')
        if len(ler_json['tarefas']) == 0: 
            print('\nA lista está vazia!\n')
            time.sleep(2)

        else:
            tarefa = input("Insira a tarefa que deseja remover (posição ou nome): ")
            encontrado = 0


            if tarefa.isdigit():
                quantLinhas = 0
                for linha in ler_json['tarefas']:
                    quantLinhas += 1
                
                if int(tarefa) > quantLinhas or int(tarefa) <= 0:
                    print('Linha não existe!\n')
                    time.sleep(2)
                
                else:
                    del ler_json['tarefas'][int(tarefa) - 1]

                    with open(todo, mode='w') as todo_json:
                        json.dump(ler_json, todo_json, indent=2)
                    print("\nTarefa removida com sucesso!\n")
                    time.sleep(2)

            else:
                for linha in ler_json['tarefas']:
                    for ignorar, task in linha.items():
                        if tarefa.lower() == task:
                            encontrado = 1
            
            
                if encontrado != 0:
                    ler_json['tarefas'] = [linha for linha in ler_json['tarefas'] if list(linha.values())[0].lower() != tarefa.lower()]

                    with open(todo, mode='w') as todo_json:
                        json.dump(ler_json, todo_json, indent=2) ###Indent para quebra de linha e recuo

                    print("\nTarefa removida com sucesso!\n")
                    time.sleep(2)
                
                else: 
                    print("\nTarefa não existe!\n") 
                    time.sleep(2)


    elif escolha in encerrar:
        break
    
    else:
        print("\nOpção não encontrada. tente novamente!\n")