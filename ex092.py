from datetime import date
dados = {}
dados['nome'] = str(input('Nome: '))
dados['idade'] = date.today().year - int(input('Ano de Nascimento: ' ))
dados['ctps'] = int(input('Carteira de Trabalho (0 para não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] - (date.today().year - dados['contratação']) + 35
    print('='*30)
for k, v in dados.items():
    print(f'- {k} tem o valor: {v}')