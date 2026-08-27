import os 
os.system('cls')

#ENTRADA
primeira_nota = float(input("Digite a primeira nota:"))
segunda_nota = float(input("Digite a segunda nota:"))
terceira_nota = float(input("Digite a terceira nota:"))

#PROCESSAMENTO
media = (primeira_nota + segunda_nota + terceira_nota)

print("media:", media)

if media <7:
    print("aluno reprovado")
else:
    print("aluno aprovado")

