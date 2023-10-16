import requests ### favor dar pip install requests 
### 95bdee2f1ae5d977391a7c77fa7bd3bc
# minha chave api da OpenWeatherMap

chaveAPI = '95bdee2f1ae5d977391a7c77fa7bd3bc'
print("Bem-vindo ao consultor de previsão do tempo.")
cidade = (input("Insira a cidade desejada: ")).title()

url = f'http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chaveAPI}&lang=pt'

retornoRequest = requests.get(url)
dados = retornoRequest.json() ### converter a resposta do link HTTPS para JSON

if retornoRequest.status_code == 200: 
    if 'cod' in dados and dados['cod'] == '404':  ### o cod remete a code e retorna o código status da resposta, ou seja
                                                  ### se retornar o clássico 404, retornará que a cidade não foi encontrada.
        print('Cidade não encontrada. Tente novamente.')
    
    else:
        print(f'\nTempo em {cidade}: {dados["weather"][0]["description"]}.')

else:
    print('Erro ao obter dados do tempo atual')