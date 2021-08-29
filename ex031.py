d1 = int(input('Digite a distância da sua viagem em KMs: '))
if d1 <= 200:
    print(f'O valor da sua passagem é de: {d1*0.5}R$')
else:
    print(f'O valor da sua passagem é de: {d1*0.45}R$')
