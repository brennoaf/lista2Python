# -*- coding: utf-8 -*-
import random
import os

animais = 'forcas/animais.txt'
alimentos = 'forcas/alimentos.txt'
objetos = 'forcas/objetos.txt'
escolhido = False #### TERMINAR WHILE DE ESCOLHER CATEGORIA
termino = False #### TERMINAR TODO O CÓDIGO

animal = ['animais', 'animal', 'bichos', 'bicho']
alimento = ['comida', 'comidas', 'alimentos', 'alimento']
objeto = ['objeto', 'objetos', 'coisas,' 'coisa', 'itens', 'items', 'item']

##### DEF PRA LIMPAR O CONSOLE
def limpa():
    os.system('cls' if os.name == 'nt' else 'clear')
############################

limpa()
print("Bem-vindo ao jogo de caça palavras!\n\nREGRAS: Você só pode errar 7 vezes.\nDigite a palavra certa e ganhará o jogo!\nNão utilize pontos finais ou quaisquer outro tipo de caractere especial no final da tentativa.\nAcentos nas palavras também são contabilizados na resposta!")


def execForca():
    global escolhido
    global escolha
    global termino
    sim = ['sim', 'yes', 's', 'y', '1']
    nao = ['não', 'nao', 'no', 'n', '2']


    erros = 0 ##Quantidade de erros inicial do  jogador
    errosRegist = [] ##Erros do jogador
    errou = False ## Verifica se o jogador errou para mostrar a variavel errosRegist

    with open(escolha, mode='r', encoding='utf-8') as escolha_lista:
        ler_txt = escolha_lista.readlines()

        ############################
        quantLinhas = 0
        for linhas in ler_txt:
            quantLinhas += 1
        ###########VER A QUANTIDADE DE LINHAS


    ################
    sorteadorPalavra = random.randint(0, quantLinhas)
    palavraSorteada = (ler_txt[sorteadorPalavra].strip()).lower()
    quantLetras = len(palavraSorteada)

    quantRest = 1
    quantDescobrir = '＿'
    while quantRest != quantLetras:
        quantRest = quantRest + 1
        quantDescobrir = quantDescobrir + '＿'
    ############SORTEANDO ANIMAL E TRANSFORMANDO A PALAVRA EM '_ _ _ _ _ _'


    ###### LOOP PARA O A CONTINUIDADE DO JOGUINHO
    concluido = False
    palavra_acerto = quantDescobrir
    while concluido == False:
        print(palavra_acerto)

        if errou == True:
            print('\nErros: ' + str(errosRegist))
        print("\nInsira a letra ou palavra para tentar adivinhar: ")
        tentativacrua = input()
        tentativa = tentativacrua.lower()
            

        #####se contem alguma letra de tentativa ou a palavra 
        if tentativa in palavraSorteada:
            limpa()
            contem = 0 ###VERIFICAR SE CONTEM A LETRA OU PALAVRA POIS EX:
                        ### SE A PALAVRA FOR TUBARÃO E PESSOA DIGITAR TUBA O CODIGO VAI EXECUTAR
                        ### MAS COM ESSA VARIAVEL VAI VERIFICAR SE DIGITOU OU A PALAVRA CERTA OU SOMENTE A LETRA


            if tentativa == palavraSorteada:
                contem = 1
                concluido = True

                print(f"Parabéns! Você acertou a palavra '{palavraSorteada}'.\nQuantidade de erros: {str(erros)}")
                print("\nDeseja jogar novamente?\nSim\nNão")
                decisao = input()

                if decisao.lower() in sim:
                    limpa()
                    print("Bem-vindo ao jogo de caça palavras!\n\nREGRAS: Você só pode errar 7 vezes.\nDigite a palavra certa e ganhará o jogo!\nNão utilize pontos finais ou quaisquer outro tipo de caractere especial no final da tentativa.\nAcentos nas palavras também são contabilizados na resposta!")
                    escolhido = False
                    break

                if decisao.lower() in nao:
                    termino = True
                    break


            posicao = 0  ##posição do scanner da letra
            for letra in palavraSorteada:
                if tentativa == palavraSorteada[posicao]:
                    palavra_acerto = palavra_acerto[:posicao] + tentativa + palavra_acerto[posicao + 1:]
                    contem = 1
                posicao += 1

            if contem == 0:
                limpa()
                print(f"Letra ou tentativa de acerto '{tentativa}' é incorreta! Tente novamente.")
                erros += 1
                print("Quantidade de erros: " + str(erros) + '\n')

                errou = True
                errosRegist.append(tentativa)

            else:
                print(f"Boa! Você acertou a letra '{tentativa}'\n\n")

        else:
            limpa()
            print(f"Letra ou tentativa de acerto '{tentativa}' é incorreta! Tente novamente.")
            erros += 1
            print("Quantidade de erros: " + str(erros) + '\n')

            errou = True
            errosRegist.append(tentativa)

        if erros > 7:
            concluido = True

            print(f"Você atingiu 8 erros! Perdeu!\nA palavra era: '{palavraSorteada}'\n")
            print("Deseja tentar novamente?\nSim\nNão")
            decisao = input()

            if decisao.lower() in sim:
                limpa()
                print("Bem-vindo ao jogo de caça palavras!\n\nREGRAS: Você só pode errar 7 vezes.\nDigite a palavra certa e ganhará o jogo!\nNão utilize pontos finais ou quaisquer outro tipo de caractere especial no final da tentativa.\nAcentos nas palavras também são contabilizados na resposta!")
                escolhido = False

            if decisao.lower() in nao:
                termino = True



while termino == False:
    while escolhido == False: 
        print("\nEstas são as categorias disponíveis para jogar: \nAnimais\nAlimentos\nObjetos\n")
        escolha = input()
        escolhaShow = escolha

        if escolha.lower() in animal:
            escolha = animais
            escolhido = True

        elif escolha.lower() in alimento:
            escolha = alimentos
            escolhido = True

        elif escolha.lower() in objeto:
            escolha = objetos
            escolhido = True

        else:
            print('Opção não encontrada. Verifique e tente novamente!\n\n')

    limpa()
    print('Vamos lá!')
    print(f'A categoria escolhida foi: {escolhaShow}')
    print("Agora tente adivinhar o seguinte:\n")
    execForca()