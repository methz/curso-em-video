print('\nDesafio relacionado ao curso de Python do Curso em Vídeo')
print('------------------------------------------------------------')
print('Autor: Marcos Oliveira')
print('Desafio: 012')
print('Aula: Curso Python #07 - Operadores Aritméticos')
print('------------------------------------------------------------')
print('Carregando o programa...')
print('Programa iniciado com sucesso')
print('------------------------------------------------------------')

preco = float(input('Digite o preço do produto (em R$): '))
desconto = 0.05  # valor fixo de 5%

print('O preço original do produto é R$ {}.'.format(preco))
print('O novo preço com 5% de desconto é R$ {}'.format(preco - (preco * desconto)))