# A prestação nao pode passar 30% do salario

casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
ano = int(input('Digite em quantos anos você quer pagar: '))

ano = ano * 12
prestacao = casa / ano
psalario =  salario * 0.30

if prestacao > psalario:
    print('\033[;31m Seu emprestimo foi negado \033[m')

elif prestacao <= psalario:
    print('\033[;32m Seu emprestimo foi aprovado \033[m')
