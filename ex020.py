import random
n1 = input('Digite um nome: ')
n2 = input('Digite o 2° nome: ')
n3 = input('Digite o 3° nome: ')
n4 = input('Digite o 4° nome: ')
ls = [n1, n2, n3, n4]
random.shuffle(ls)
print(ls)
