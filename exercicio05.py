peso = float(input("Digite o seu peso (kg): ").replace(",","."))
altura = float(input("Digite sua altura (m): ").replace(",","."))

imc = peso / (altura**2)


if imc < 18:
    print(f"Você tem {imc}. Você tem magreza")
if imc >=18:
    print(f"Você tem {imc}. Você é normal")




