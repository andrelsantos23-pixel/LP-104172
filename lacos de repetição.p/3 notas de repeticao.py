import os
os.system

for i in range(1, 4):
    nota = float(input(f"Digite a {i}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f"\nMédia final: {media:.2f}")

if media >= 7.0:
    print("Situação: APROVADO")
elif media < 4.0:
    print("Situação: REPROVADO")
else:
    print("Situação: EM RECUPERAÇÃO")