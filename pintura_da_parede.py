# 1l de tinta para 2m²

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))

area = larg * alt

print('Sua parede tem a dimensão de {}x{} e sua area é de {}m²'.format(larg, alt, area))
print('Para pintar sua parede serão necessários {:.3f} litros de tinta'.format(area / 2))
