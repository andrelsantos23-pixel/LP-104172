import os
os.system('cls')

soma_pares = qtd_pares = qtd_impares = soma_geral = qtd_geral = 0

numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    soma_geral += numero
    qtd_geral += 1
    
    if numero % 2 == 0:
        soma_pares += numero
        qtd_pares += 1
    else:
        qtd_impares += 1
        
    numero = int(input("Digite um número (0 para sair): "))

if qtd_geral > 0:
    print(f"\nPares: {qtd_pares} | Ímpares: {qtd_impares}")
    print(f"Média dos pares: {soma_pares / qtd_pares if qtd_pares > 0 else 0:.2f}")
    print(f"Média geral: {soma_geral / qtd_geral:.2f}")
    