from subprocess import check_output

frase = input("Digite uma frase: ")

palavras = frase.split()

contagem = {}

for palavras in palavras:
    if palavras in contagem:
        contagem[palavras] += 1
    else:
        contagem[palavras] = 1

print("Contagem de palavras: ")
print(contagem)
