c = ('\033[m',  # 0 - sem cores
     '\033[0;30;41m',  # 1 - Vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m')     # 6 - branco


def ih(txt):
    from time import sleep
    tit(f'Acessando o manual do comando \'{txt}\'', 6)
    sleep(0.5)
    print(c[4],  end='')
    help(txt)
    print(c[0], end='')


def tit(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('='*tam)
    print(f'  {msg}')
    print('='*tam)
    print(c[0], end='')


while True:
    tit('Sistema de ajuda', 2)
    u = str(input('Função ou biblioteca > '))
    if u.upper() == 'FIM':
        break
    ih(u)
tit('Finalizando...', 1)
