import os
os.system('cls')

import os

soma_salarios = total_pessoas = 0
maior_idade = menor_idade = None
mulheres_5k = 0

opcao = 0

while opcao != 3:
    print("\n--- MENU ---")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")
    
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        os.system('cls' if os.name == 'nt' else 'clear') 

        idade = int(input("Idade: "))
        sexo = input("Sexo (M/F): ").strip().upper()
        salario = float(input("Salário (R$): "))

        soma_salarios += salario
        total_pessoas += 1

        if maior_idade is None or idade > maior_idade:
            maior_idade = idade
        if menor_idade is None or idade < menor_idade:
            menor_idade = idade

        if sexo == 'F' and salario >= 5000:
            mulheres_5k += 1

    elif opcao == 2:
        if total_pessoas > 0:
            print("\n" + "=" * 35)
            print(f"a) Média de salário: R$ {soma_salarios / total_pessoas:.2f}")
            print(f"b) Maior idade: {maior_idade} | Menor idade: {menor_idade}")
            print(f"c) Mulheres com salário >= R$ 5.000: {mulheres_5k}")
            print("=" * 35)
        else:
            print("\nNenhuma pessoa cadastrada ainda!")

    elif opcao == 3:
        print("\nPrograma encerrado.")
    else:
        print("\nOpção inválida!")