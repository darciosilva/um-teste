import math
co = float(input('digite o valor do cateto oposto: '))
ca = float(input('digite o valor do cateto adjacente: '))
hi = math.hypot(co, ca)
print('o valor da hipotenusa é de —> {:.2f}'.format(hi))