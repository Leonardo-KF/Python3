from exa22 import moedas

pre = float(input('Digite o valor do produto R$: '))
print(f'A metade de {moedas.val(pre)} é {moedas.met(pre, f=True)}')
print(f'Aumentando 10%, temos {moedas.ju(pre, 10, f=True)}')
print(f'Reduzindo 13%, temos {moedas.des(pre, 13, f=True)}')