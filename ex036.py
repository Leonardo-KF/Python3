v1 = float(input('Digite o valor do imóvel que você pretende adquirir R$: '))
v2 = float(input('Digite o seu salário mensal R$: '))
v3 = int(input('Digite em quantos anos você deseja quitar: '))
meses = v3 * 12
parc = v1 / meses
if parc <= (v2 * 0.3):
    print(f'Seu empréstimo foi aprovado!! O valor mensal a ser pago será de R$:{parc}')
else:
    print('Infelizmente seu financiamento não foi aprovado!')
