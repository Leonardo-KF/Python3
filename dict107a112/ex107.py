from exa22 import moedas
p = float(input('Digite o preço do produto: R$ '))
print(f'A metade do preço: {moedas.met(p)}')
print(f'O dobro do preço: {moedas.dob(p)}')
print(f'Aumentando 10%: {moedas.ju(p, 10)}')
print(f'Reduzindo 13%: {moedas.des(p, 13)}')