import random
import os

print('Tente adivinhar o Número(0-100)')
valor = random.randint(1, 10)
a = ''
cont = 1
while a != valor:
    print(f'{cont}° tentativa.')
    a = int(input('Digite um número: '))
    if a > valor:
        print(f'{a} é maior que o Valor. Tente novamente!')
        print('------------------------')
        cont = cont + 1
    elif a < valor:
        print(f'{a} é menor que o Valor. Tente novamente!')
        print('------------------------')
        cont = cont + 1
    else:
        print(f'Você acertou em {cont} tentativas. O valor era {valor}. ')
