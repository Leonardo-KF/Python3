from random import randint
print('-' * 20)
print('PAR OU ÍMPAR')
print('-' * 20)
cv = 0
while True:
    comp = randint(1, 10)
    u = ' '
    while u not in 'PI':
        u = str(input('Você escolhe Par ou Ímpar: ')).strip().upper()[0]
    nu = int(input('Digite o numero que você escolheu: '))
    res = comp + nu
    r = res % 2
    if u == 'P' and r == 0:
        cv += 1
        print(f'Você ganhou! Você esolheu PAR e o Computador escolheu ímpar\n'
              f'Você digitou {nu} e o computador digitou {comp}\n'
              f'E o resultado foi {res} que é PAR\n'
              f'PARABÉNS!!!')
    elif u == 'I' and r == 1:
        cv += 1
        print(f'Você ganhou! Você escolheu ÍMPAR e o computador escolheu par\n'
              f'Você digitou {nu} e o computador digitou {comp}\n'
              f'E o resultado foi {res} que é ÍMPAR\n'
              f'PARABÉNS!!!')
    else:
        print('=' * 15)
        print('GAME OVER')
        print('=' * 15)
        print(f'Você jogou {nu} e o Computador jogou {comp} e o resultado foi {res}')
        print(f'Você perdeu!! Você venceu {cv} vezes!')
        break
