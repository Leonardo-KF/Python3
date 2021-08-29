def tit(txt):
    print('=' * 50)
    print(f'{txt:^50}')
    print('=' * 50)


def ops(lst):
    for i, item in enumerate(lst):
        print(f'\033[33m{i+1} - \033[m\033[36m{item}\033[m')
    print('='*50)
    u = lint('Digite o numero da opção desejada: ')
    return u


def lint(n):
    while True:
        try:
            n1 = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um numero inteiro! \033[m')
            continue
        else:
            return n1
