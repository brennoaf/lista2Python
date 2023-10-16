### minha chave API cd2723139453d9510cfa0a90

import requests ### dar pip install requests
import os

chaveAPI = 'cd2723139453d9510cfa0a90'

consulta = ['consulta', 'consultar', 'buscar', '1']
converter = ['converter', 'converte', 'conversão', 'conversao', '2']
escolhido = False

urlLista = f'https://v6.exchangerate-api.com/v6/{chaveAPI}/codes'


while escolhido == False:   
    print('\nBem-vindo ao consultor de câmbios entre moedas!\nO que deseja fazer?')
    print('1. Consultar moedas\n2. Converter uma moeda')
    escolha = input()

    if escolha in consulta:
        escolha = consulta
        escolhido = True

    elif escolha in converter:
        escolha = converter
        escolhido = True

    else:
        print("Opção não encontrada. Tente novamente.\n")


    if escolha == consulta:
        escolhido = False
        resposta = requests.get(urlLista)
        dados = resposta.json() ### converte o dado recebi HTTPS em JSON para manipular

        if resposta.status_code == 200:
            moedasLista = dados['supported_codes']

            print("Lista de moedas suportadas:")
            for linhas in moedasLista:
                print(linhas)

    if escolha == converter:
        os.system('cls')
        print("Insira sua moeda inicial: ") ### Inserir moeda antes de converter
        moedaInicial = (input()).upper()

        urlMoedas = f'https://v6.exchangerate-api.com/v6/{chaveAPI}/latest/{moedaInicial}'
        respostaInicial = requests.get(urlMoedas)
        dadosInicial = respostaInicial.json() ### converte o dado recebi HTTPS em JSON para manipular

        respostaLista = requests.get(urlLista)
        dadosLista = respostaLista.json()

        moedaLista = dadosLista['supported_codes']
        achouInicial = achouFinal = 0
        for linha in moedaLista:
            if moedaInicial in linha:
                print("\nInsira para qual moeda deseja converter: ")
                moedaAlvo = (input()).upper()
                achouInicial=1

        if achouInicial == 1:
                for linha in moedaLista:
                    if moedaAlvo in linha:
                        certo = False
                        while not certo:
                            try:
                                quantia = float(input('\nInsira a quantia: '))
                                certo = True
                            
                            except ValueError: 
                                print('Valor inserido é impossível! Verifique e tente novamente!')

                        cambioMoeda = dadosInicial['conversion_rates'][moedaAlvo]
                        conversao = quantia * cambioMoeda

                        print(f"\n{quantia} {moedaInicial} é igual a {conversao:.2f} {moedaAlvo}")
                        achouFinal = 1
        
        if achouInicial != 1 or achouFinal != 1:
            print("\nMoeda não encontrada! Tente novamente.")
            escolhido = False