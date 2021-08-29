from random import randint
from time import sleep
print('-=-' * 20)
print('Tente descobrir o numero de 0 á 5...')
print('-=-' * 20)
t1 = randint(0, 5)
u = int(input('Digite o numero de sua escolha: '))
print('PROCESSANDO...')
sleep(3)
if u == t1:
    print('Parabéns você acertou!!')
else:
    print(f'Você errou, o numero escolhido foi: {t1}')
