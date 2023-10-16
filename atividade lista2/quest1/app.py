def calcularMedia(notas):
    return sum(notas) / len(notas)

def condicoesNota(media):
    if media >= 9:
        return 'A'
    elif media >= 8:
        return 'B'
    elif media >= 7:
        return 'C'
    elif media >= 6:
        return 'D'
    elif media >= 5:
        return 'E'
    else:
        return 'F'

quantNotas = int(input("Quantas notas você deseja inserir? "))
notas = []
for i in range(quantNotas):
    notas.append(float(input(f"Informe a nota {i + 1} (0 a 10): ")))

media = calcularMedia(notas)
conceito = condicoesNota(media)

print(f"A média das notas é: {media:.2f}")
print(f"A média correspondente é: {conceito}")