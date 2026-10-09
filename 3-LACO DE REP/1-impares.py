import os
import time
os.system('cls')

print('MOSTRANDO OS NÚMEROS ÍMPARES ENTRE 1 E 20 ')
for i in range(1,21):
    if i % 2 == 0:
        print(f'{i} é par')
