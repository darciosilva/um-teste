preco = float(input('coloque o valor do preço: '))
porcent = float(input('coloque quantos porcentos de desconto: '))
descont = (preco*porcent)/100
descon = preco-descont
print('R${} com {}% de desconto fica R${}'.format(preco, porcent, descon))
