#minha solucao
#altura = float(input('Informe a altura da sua parade: '))
#largura = float(input('Informe a largura da sua parede: '))
#area = altura * largura
#print('A área é de {}'.format(area))
#tintaNecessaria = area / 2
#print('Para pintar esta parede serão necessarios {} litros de tinta'.format(tintaNecessaria))

#solucao do curso
larg = float(input('Informe a largura da sua parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
