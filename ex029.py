vel = int(input('Digite qual a velocidade em KM/H: '))
if vel > 80:
    print(f'Você foi multado por andar á {vel}KM/H!! '
          f'O valor a ser pago é de: {(vel-80)*7}R$')
else:
    print('Boa Viagem!')
