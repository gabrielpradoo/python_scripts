# Dolar = 3.88 R$
# Euro = 4.39 R$
# Libra = 5.08 R$
# Bitcoin = 19776.15 R$

resp = str('SIM')

while resp != 'NÂO' and resp == 'SIM':
    moeda = input('Digite para qual moeda você que converter:\n Dolar, Euro, Libra, Bitcoin: ')
    moeda = moeda.upper()
    real = float(input('Digite o valor em reais. R$'))

    if moeda == 'DOLAR':
        print('R${:.2f} é igual a U${:.2f} .'.format(real, (real / 3.88)))

    elif moeda == 'EURO':
        print('R${:.2f} é igual a €{:.2f} .'.format(real, (real / 4.39)))

    elif moeda == 'LIBRA':
        print('R${:.2f} é igual a £{:.2f} .'.format(real, (real / 5.08)))

    elif moeda == 'BITCOIN':
        print('R${:.2f} é igual a ₿{:.2f} .'.format(real, (real / 19776.15)))

    else:
        print('Você digitou algo errado.')

    resp = input('Deseja pesquisar de novo. SIM ou NAO? ')
    resp = resp.upper()
