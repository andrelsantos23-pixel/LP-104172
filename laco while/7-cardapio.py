import os
os.system('cls')

total_conta = 0
deseja_continuar = "s"

print("=" * 35)
print("       CARDÁPIO DO RESTAURANTE     ")
print("=" * 35)
print("1 - Picanha         - R$ 25,00")
print("2 - Lasanha         - R$ 20,00")
print("3 - Strogonoff      - R$ 18,00")
print("4 - Bife Acebolado  - R$ 15,00")
print("5 - Pão com Ovo     - R$  5,00")
print("=" * 35)

while deseja_continuar.lower() == "s" or deseja_continuar.lower() == "sim":
    opcao = int(input("\nDigite o número do prato desejado: "))

    if opcao == 1:
        total_conta += 25.00
        print("-> Picanha adicionada!")
    elif opcao == 2:
        total_conta += 20.00
        print("-> Lasanha adicionada!")
    elif opcao == 3:
        total_conta += 18.00
        print("-> Strogonoff adicionado!")
    elif opcao == 4:
        total_conta += 15.00
        print("-> Bife Acebolado adicionado!")
    elif opcao == 5:
        total_conta += 5.00
        print("-> Pão com Ovo adicionado!")
    else:
        print("Opção inválida! Nenhum item foi adicionado.")

    deseja_continuar = input("\nDeseja escolher outro prato? (s/n): ")

print("\n" + "=" * 35)
print(f"Total a pagar: R$ {total_conta:.2f}")
print("Obrigado pelo pedido e bom apetite!")
print("=" * 35)