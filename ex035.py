t1 = float(input('Digite o tamanho da primeira reta: '))
t2 = float(input('Digite o tamanho da segunda reta: '))
t3 = float(input('Digite o tamanho da terceira reta: '))
v = (t1 - t2) < t3 < (t1 + t2)
if v:
    print('Elas podem formar um triângulo!')
else:
    print('Elas não podem formar um triângulo!')
