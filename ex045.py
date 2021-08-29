from time import sleep
from random import randint
print('\033[;34m-=-\33[m' * 12)
print('\033[;44mVamos jogar pedra, papel, tesoura...\033[m')
print('\033[;34m-=-\33[m' * 12)
sleep(1)
e1 = str(input('\033[35mEscolha\n'
               'Pedra\n'
               'Papel\n'
               'Tesoura\n'
               'Digite sua escolha\033[m: ')).strip().lower()
comp = randint(1, 3)
if comp == 1:
    e3 = 'pedra'
elif comp == 2:
    e3 = 'papel'
elif comp == 3:
    e3 = 'tesoura'
# regras do jogo
if e1 == 'papel' and e3 == 'papel':
    r1 = 'Empatou!'
elif e1 == 'pedra' and e3 == 'papel':
    r1 = 'Você perdeu!'
elif e1 == 'tesoura' and e3 == 'papel':
    r1 = 'Você venceu!'
elif e1 == 'pedra' and e3 == 'pedra':
    r1 = 'Empatou!'
elif e1 == 'tesoura' and e3 == 'pedra':
    r1 = 'Você perdeu!'
elif e1 == 'papel' and e3 == 'pedra':
    r1 = 'Você venceu!'
elif e1 == 'papel' and e3 == 'tesoura':
    r1 = 'Você perdeu!'
elif e1 == 'pedra' and e3 == 'tesoura':
    r1 = 'Você venceu!'
elif e1 == 'tesoura' and e3 == 'tesoura':
    r1 = 'Empatou!'
else:
    print('Escolha invalida! Tente Novamente!')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('\033[32m -=-' * 17)
print(f'{r1} Você escolheu {e1} e o computador escolheu {e3}!')
print('\033[32m -=-' * 17)