from math import cos, sin, radians, tan
a1 = float(input('Digite um ângulo: °'))
cos = cos(radians(a1))
sen = sin(radians(a1))
tg = tan(radians(a1))
print(f'O seno do angulo {a1}° é: {sen:.2f}°')
print(f'O cosseno do angulo {a1}° é: {cos:.2f}°')
print(f'A tangente do angulo {a1}° é: {tg:.2f}°')
