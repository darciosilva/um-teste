import math
angulo = float(input('digite o angulo ≈> '))
radiano = math.radians(angulo)
sen = math.sin(radiano)
cos = math.cos(radiano)
tan = math.tan(radiano)
print('o valor do seno é {:.2f}'.format(sen))
print('o valor do cosseno é {:.2f}'.format(cos))
print('o valor do tangente ê {:.2f}'.format(tan))