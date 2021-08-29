from random import randint
from time import sleep
print('Tente advinhar o numero que eu escolhi!!')
sleep(1)
comp = randint(0, 10)
tu = 1
user = int(input('Digite o seu primeiro palpite: '))
while user != comp:
    tu += 1
    if user < comp:
        print('Não acertou! O numero que eu escolhi é maior!')
    else:
        print('Não acertou! O numero que eu escolhi é menor!')
    user = int(input('Tente novamente! Sua nova escolha é: '))
print(f'Você acertou em {tu} tentativas!')