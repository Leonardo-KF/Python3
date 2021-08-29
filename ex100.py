from random import randint
from time import sleep


def sort(val):
    print(f'Sorteando {val} valores: ', end='')
    for c in range(0, val):
        c = randint(0, 11)
        sleep(0.4)
        print(c, end=' ')
        nume.append(c)
    print('FIM!')


def somp(lst):
    r = 0
    for c in lst:
        if c % 2 == 0:
            r += c
    print(f'Somando os valores pares de {lst} temos a soma de {r}')


nume = []
sort(5)
somp(nume)
