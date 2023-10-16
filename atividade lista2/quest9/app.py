filmes = ['Aquaman 2', 'O som do silêncio', 'Transformers 5', 'Patrulha Canina']
horas = [['12:00', '18:00', '21:00'], ['13:00', '15:30', '18:00'], ['12:30', '20:00'],  ['11:00', '13:00', '19:00']]

reservas = 'reservas/reservas.txt'
def fazer_reserva(nome, filme, horario, ingressos):
    with open(reservas, "a", encoding='utf-8') as arquivo:
        arquivo.write(f"Nome: {nome}, Filme: {filme}, Horário: {horario}, Ingressos: {ingressos}\n")
    print("Reserva feita com sucesso!")

nome = input("Insira o seu nome: ")

# Mostrar os filmes e horários disponíveis
print("Bem-vindo ao sistema de reserva de cinema.\nFilmes disponíveis:")
for i, filme in enumerate(filmes):
    print(f"{i + 1}. {filme}")
escolhaFilme = int(input("Escolha o número do filme desejado: ")) - 1

if escolhaFilme < 0 or escolhaFilme >= len(filmes):
    print("Escolha inválida. Saindo do programa.")

else:
    filmeEscolhido = filmes[escolhaFilme]
    print(f"Horários disponíveis para {filmeEscolhido}:")

    for j, horario in enumerate(horas[int(escolhaFilme) - 1]):
        print(f"{j + 1}. {horario}")
    escolhaHorario = input("Escolha o número do horário desejado: ")


    if not escolhaHorario.isdigit() or int(escolhaHorario) < 1 or int(escolhaHorario) > len(horas[int(escolhaFilme) - 1]):
        print("Escolha inválida. Saindo do programa.")

    else:

        horarioEscolhido = horas[int(escolhaFilme) - 1][int(escolhaHorario) - 1]
        numIngressos = int(input("Quantos ingressos deseja comprar? "))

        fazer_reserva(nome, filmeEscolhido, horarioEscolhido, numIngressos)