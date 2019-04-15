from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('========== JO KEN PO ==========')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

sleep(0.5)
print('\033[1;34mJO\033[m')
sleep(1)
print('\033[1;35mKEN\033[m')
sleep(1)
print('\033[1;36mPO!!\033[m')
sleep(1)



print('=-=' *10)
print('Computador jogou {}.'.format(itens[pc]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('=-=' *10)



if pc == 0 :                     # pc escolheu pedra
    if jogador == 0:
        print('\033[;33mEMPATE!\033[m')
    elif jogador == 1:
        print('\033[;32mJOGADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[;31mCOMPUTADOR VENCE!\033[m')
    else:
        print('JOGADA INVÁLIDA!')


elif pc == 1:                    # pc escolheu papel
    if jogador == 0:
        print('\033[;31mCOMPUTADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[;33mEMPATE!\033[m')
    elif jogador == 2:
        print('\033[;32mJOGADOR VENCE!\033[m')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 2:                   # pc escoleu tesoura
    if jogador == 0:
        print('\033[;32mJOGADOR VENCE!\033[m')
    elif jogador == 1:
        print('\033[;31mCOMPUTADOR VENCE!\033[m')
    elif jogador == 2:
        print('\033[;33mEMPATE!\033[m')
    else:
        print('JOGADA INVÁLIDA!')
