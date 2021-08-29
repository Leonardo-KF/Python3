from time import sleep


def cont(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        ct = i
        while ct <= f:
            print(f'{ct} ', end='', flush=True) # flush é para o caso de não aparecer de forma gradual os numeros
            sleep(0.4)
            ct += p
        print('FIM!')
    else:
        ct = i
        while ct >= f:
            print(f'{ct} ', end='', flush=True)
            sleep(0.4)
            ct -= p
        print('FIM!')


cont(1, 10, 1)
cont(f=0, i=10, p=2)
print('-' * 8)
print('Contador')
print('-' * 8)
n1 = int(input('Digite o valor que deseja inciar a contagem: '))
n2 = int(input('Digite o valor que deseja que termine a contagem: '))
n3 = int(input('Digite o passo da contagem: '))
cont(n1, n2, n3)
