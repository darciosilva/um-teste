alt = float(input('digite a altura da sua parede '))
larg = float(input('digite a largura da sua parede '))
m2 = alt * larg
print ('a dimensão da sua parede é de {}×{} e tem {}m² '.format(alt, larg, m2))
tinta = m2/2
print('para pintar {}m² você precisara de {}l de tinta '.format(m2, tinta))