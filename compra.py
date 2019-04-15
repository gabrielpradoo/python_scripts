print('\033[1;30;41m========== LOJAS AMERICANAS ==========\033[m')

preco = float(input('Digite o valor da compra: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque.')
print('[ 2 ] à vista no cartão.')
print('[ 3 ] 2x no cartão.')
print('[ 4 ] 3x ou mais no cartão.')
pag = int(input('Qual a opção de pagamento? '))

if pag == 1:
    valor = preco - (preco * 0.10)
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, valor))

elif pag == 2:
    valor = preco - (preco * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preco, valor))

elif pag == 3:
    print('Sua compra vai custar R$',preco)

elif pag == 4:
    parcela = int(input('Quantas parcelas? '))
    valor = ((preco * 0.20) + preco)
    vezes = valor / parcela

    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcela, vezes))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, valor))
