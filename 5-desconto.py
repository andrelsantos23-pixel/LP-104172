import os
os.system('cls')

print('= SOLICITANDO DADOS=')
valor= float(input('Digite o valor: '))

#CALCULANDO
#Descontando 10%.
desconto = valor * 0.10
valor_com_desconto = valor - desconto

print('\n= EXIBINDO DADOS =')
print("valor com desconto final: " , valor_com_desconto)