print('\nDesafio relacionado ao curso de Python do Curso em Vídeo')
print('------------------------------------------------------------')
print('Autor: Marcos Oliveira')
print('Desafio: 013')
print('Aula: Curso Python #07 - Operadores Aritméticos')
print('------------------------------------------------------------')
print('Carregando o programa...')
print('Programa iniciado com sucesso')
print('------------------------------------------------------------')

salario = float(input('Digite seu salário (em R$): '))
aumento = 0.15  # valor fixo de 5%

print('O salário atual é R$ {}.'.format(salario))
print('O salário com 15% de aumento é R$ {}'.format(salario + (salario * aumento)))