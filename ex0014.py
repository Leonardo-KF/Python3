km = float(input('Digite a quantidade percorrida de KMs: '))
d = float(input('Digite a quantidade de dias que o carro foi alugado: '))
tkm = km * 0.15
td = d * 60
t = tkm + td
print(f'Você rodou {km}KM em {d} dias, o valor a ser pago é de: {t}R$ ')
