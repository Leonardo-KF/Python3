from time import sleep
while True:
    n1 = int(input('Digite o numero para qual deseja a tabuada (numero negativo p/ parar): '))
    if n1 < 0:
        break
    for c in range(1, 11):
        print(f'{c} X {n1} = {c*n1}')
print('Finalizando...')
sleep(1)
print('Obrigado por utilizar nosso programa!')
