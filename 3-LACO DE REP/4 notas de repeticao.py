import os
os.system('cls')

print('= Solicitando notas =')
soma = 0

for i in range(4):
    nota = float(input('Digite uma nota: '))
    soma = soma + nota

# PROCESSAMENTO.
media = soma / 4

# SAIDA.
print('\n= Exibindo resultados =')
print(f'Média: {media}')

