t1 = float(input('Digite o tamanho da primeira reta: '))
t2 = float(input('Digite o tamanho da segunda reta: '))
t3 = float(input('Digite o tamanho da terceira reta: '))
if t1 < t2 + t3 and t2 < t3 + t1 and t3 < t1 + t2:
    print('Elas podem formar um triângulo! Será um triangulo ', end='')
    if t1 == t2 and t2 == t3:
        print('equilatero!')
    elif t1 != t2 and t2 != t3 and t3 != t1:
        print('escaleno!')
    else:
        print('isósceles!')
else:
    print('Eles não podem formar um triangulo!')