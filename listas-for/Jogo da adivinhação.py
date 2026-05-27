import random

numero_secreto = random.randint(1, 20)

palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Digite um número entre 1 e 20: "))

    if palpite < numero_secreto:
        print("O número secreto é MAIOR!")

    elif palpite > numero_secreto:
        print("O número secreto é MENOR!")

print("Parabéns! Você acertou o número secreto!")