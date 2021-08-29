from exer115.lib.interface import *
from time import sleep
from exer115.lib.arquivo import *
arq = 'curso.txt'
if not earq(arq):
    criaarq(arq)
while True:
    tit('Menu Principal')
    resp = ops(['Cadastrar nova pessoa', 'Ver pessoas cadastradas', 'Sair do programa'])
    if resp == 1:
        tit('Cadastro de uma pessoa')
        nome = str(input('Nome: '))
        idade = lint('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(0.5)
    elif resp == 2:
        tit('Exibindo pessoas cadastradas')
        lerarqui(arq)
        sleep(0.5)
    elif resp == 3:
        sleep(0.5)
        tit('Finalizando...')
        break
    else:
        print('\033[31mA opção que você digitou é invalida! Por favor tente novamente!\033[m')
        sleep(1)
sleep(1)
print('Obrigado por utilizar essa solução! Volte sempre!')
