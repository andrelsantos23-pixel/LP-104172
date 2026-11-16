import os
os.system('cls')

def inflacionar_preco(preco_produto):
    if preco_produto >= 100:
        resultado = preco_produto * 1.20 
    else:
        resultado = preco_produto * 1.10
    return resultado

print('= SOLICITANDO DADOS =')
preco_produto = float(input('Digite o preco do produto: '))

# Chamando a funcão.
preco_inflacionado = inflacionar_preco(preco_produto)

print('\n= EXIBINDO DADOS =')
print(f'Preco inicial: R$ {preco_produto}')
print(f'Preco inflacionado: R$ {preco_inflacionado}')