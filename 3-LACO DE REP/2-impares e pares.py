import os
os.system('cls')

pares = 0
impares = 0

for i in range(1, 21):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares = impares + 1

print(f'Quantidades de números pares: {pares}')
print(f'Quantidades de números ímpares: {impares}')

print('FIM')