print('\nDesafio relacionado ao curso de Python do Curso em Vídeo')
print('------------------------------------------------------------')
print('Autor: Marcos Oliveira')
print('Desafio: 010')
print('Aula: Curso Python #07 - Operadores Aritméticos')
print('------------------------------------------------------------')
print('Carregando o programa...')
print('Programa iniciado com sucesso')
print('------------------------------------------------------------')

dinheiro = float(input('Digite o valor presente na sua carteira de investimentos (em R$): '))
cotacao = 4.62  # ajuste do dólar no dia 08/03/2020, às 19:55

print('Seu saldo atual é de R$ {}'.format(dinheiro))
print('Com o saldo acima você pode adquirir US$ {:.2f}'.format(dinheiro/cotacao))
