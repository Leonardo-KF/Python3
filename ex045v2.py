from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
ej = int(input('Faça a sua escolha:\n'
               '[ 0 ] PEDRA\n'
               '[ 1 ] PAPEL\n'
               '[ 2 ] TESOURA\n'
               'Sua escolha é: '))
print('-=-' * 10)
print(f'Você escolheu {itens[ej]}')
print(f'O computador escolheu {itens[comp]}')
print('-=-' * 10)
if ej == 0:  # jogador escolheu pedra
    if comp == 0:
        res = 'EMPATE'
    elif comp == 1:
        res = 'VOCÊ PERDEU'
    elif comp == 2:
        res = 'VOCÊ VENCEU'
elif ej == 1:  # jogador escolheu papel
    if comp == 0:
        res = 'VOCÊ VENCEU'
    elif comp == 1:
        res = 'EMPATOU'
    elif comp == 2:
        res = 'VOCÊ PERDEU'
elif ej == 2:  # jogador escolheu tesoura
    if comp == 0:
        res = 'VOCÊ PERDEU'
    elif comp == 1:
        res = 'VOCÊ VENCEU'
    elif comp == 2:
        res = 'EMPATOU'
else:
    print('Escolha invalida! Tente novamente!')
print(f'{res}!')
