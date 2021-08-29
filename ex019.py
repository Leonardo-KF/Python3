from random import choice
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('digite o nome do aluno 3: ')
a4 = input('digite o nome do aluno 4: ')
ls = [a1, a2, a3, a4]
ch = choice(ls)
print(f'O escolhido foi o: {ch}')
