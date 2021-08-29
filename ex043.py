h = float(input('Digite sua altura em metros: '))
p = float(input('Digite seu peso: '))
imc = p / (h * h)
if imc < 18.5:
    ind = 'Abaixo'
elif imc < 25:
    ind = 'Peso ideal'
elif imc < 30:
    ind = 'Sobrepeso'
elif imc < 40:
    ind = 'Obesidade'
else:
    ind = 'Obesidade mórbida'
print(f'O seu imc é de {imc:.2f} e o seu status é: {ind}')
