def ar(l, c):
    a = l * c
    print(f'A área do terreno de {l}m de largura e {c}m de comprimento é : {a}m²')


print('     Medidor de terrenos')
print('-' * 30)
l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento: '))
ar(l, c)
