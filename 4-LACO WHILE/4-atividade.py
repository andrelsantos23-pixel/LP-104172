import os
import time
os.system('cls')

login_correto = "Lukitos"
senha_correto = "LC14045"

while True:
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    if login == login_correto and senha == senha_correta:
        print('Login realizado com sucesso!')
        break
    else:
        print('Login ou senha incorretos. Tente novamente.')
        time.sleep(2)
        os.system('cls')

        print('=== FIM ====')