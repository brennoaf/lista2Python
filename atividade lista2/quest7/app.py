import random

randomNumero= random.randint(1, 100)

print("Bem-vindo ao jogo de adivinhação!")
fim = False

while fim == False:

    tentativa = int(input("Tente adivinhar o número (entre 1 e 100): "))

    if tentativa < randomNumero:
        print("Tente um número maior!")

    elif tentativa > randomNumero:
        print("Tente um número menor!")

    else:
        print("Parabéns! Você adivinhou o número!")
        fim = True