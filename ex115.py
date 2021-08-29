def tit(txt):
    print('=' * 50)
    print(f'{txt:^50}')
    print('=' * 50)


def ops(i, t):
    print(f'\033[33m{i} - \033[m\033[36m{t}\033[m')


def lint(n):
    while True:
        try:
            n1 = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um numero inteiro! \033[m')
            continue
        else:
            return n1


from time import sleep
while True:
    tit('Menu Principal')
    ops(1, 'Ver pessoas cadastradas')
    ops(2, 'Cadastrar nova Pessoa')
    ops(3, 'Sair do Sistema')
    print('=' * 50)
    u = lint('Digite a opção desejada: ')
    while True:
        if u > 3 or u < 1:
            print('\033[31mA opção que você digitou é invalida! Por favor tente novamente!\033[m')
            u = lint('Digite a opção desejada: ')
        else:
            break
    if u == 1:
        tit('Opção 1')
        sleep(0.5)
    if u == 2:
        tit('Opção 2')
        sleep(0.5)
    else:
        break
tit('Finalizando...')
sleep(1)
print('Obrigado por utilizar essa solução! Volte sempre!')
n1 = (1, 2, 4, 5)
print(all(n1))