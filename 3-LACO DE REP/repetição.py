import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARIAVEL. ')
soma = 0

print(f'Valor INICIAL da variável soma: {soma}')

for i in range(3):
    num = int(input('\nDigite um número para somar:'))
    soma = soma + num
    print(f'Valor TEMPORÁRIO da variável soma: {soma}')
    
    print(f'\nValor FINAL da variável soma: {soma}')
