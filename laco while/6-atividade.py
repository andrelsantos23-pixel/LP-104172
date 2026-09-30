import os
import time
os.system('cls')

login_salvo = 'Marta'
senha_salva = '@123'
tentativas = 1

while True:
    if tentativas <= 3:
        print(f'Tentativa: {tentativas}:')
        login = input('Digite o login: ')
        senha = input('Digite a senha: ')
        tentativas += 1

        if login == login_salvo and senha == senha_salva:
            print('Bem-vindo!')
            break
    else:
        print('\nLogin ou senha invalido.')
        print('Tente novamente! \n')
        input('Pressione uma tecla para continuar ... ')
        os.system('cls')
else:
    print('= FIM =')
