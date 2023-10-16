def calculoIMC(peso, altura):
    return peso / (altura * altura)

peso = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite a sua altura em metros: "))

imc = calculoIMC(peso, altura)

print(f"Seu Índice de Massa Corporal (IMC) é {imc:.2f}.")