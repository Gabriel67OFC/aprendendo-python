notas = []
for i in range(4):
    nota = float(input(f"Digite a {i+1} nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas do aluno:", notas)
print(f"Média: {media:.2}")

if media >= 7.0:
    print("Aprovado")
else:
    print("Recuperação")