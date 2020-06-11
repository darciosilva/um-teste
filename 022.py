nome = str(input('digite seu nome completo: ')).strip()

print('seu nome com letras maiusculas {}'.format(nome.upper()))
print('seu nome com letras minusculas {}'.format(nome.lower()))
print('seu nome com as primeiras letras maiusculas {}'.format(nome.title()))
print('seu nome tem inteiro tem {} letras'.format(len(nome) -nome.count(' ')))
print('seu primeiro nome tem {}'.format(nome.find(' ')))