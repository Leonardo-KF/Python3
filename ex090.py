boletim = dict()
boletim['nome'] = str(input('Nome: '))
boletim['media'] = float(input('Digite a sua média: '))
if boletim['media'] < 5:
    boletim['situação'] = 'Reprovado'
elif boletim['media'] < 7:
    boletim['situação'] = 'Recuperação'
else:
    boletim['situação'] = 'Aprovado'
print('='*30)
for k, v in boletim.items():
    print(f'- {k} é igual a {v}')