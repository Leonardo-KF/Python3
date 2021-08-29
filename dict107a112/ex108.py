from exa22 import moedas

pre = float(input('Digite o preço do produto R$: '))
print(f'A metade de {moedas.val(pre)} é: {moedas.val(moedas.met(pre))}')
print(f'O dobro de {moedas.val(pre)} é: {moedas.val(moedas.dob(pre))}')
print(f'Aumentando 10%, temos: {moedas.val(moedas.ju(pre, 10))}')