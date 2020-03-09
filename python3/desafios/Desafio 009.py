print('\nDesafio relacionado ao curso de Python do Curso em Vídeo')
print('------------------------------------------------------------')
print('Autor: Marcos Oliveira')
print('Desafio: 009')
print('Aula: Curso Python #07 - Operadores Aritméticos')
print('------------------------------------------------------------')
print('Carregando o programa...')
print('Programa iniciado com sucesso')
print('------------------------------------------------------------')

x = int(input('Digite um número inteiro: '))

print('-------------------------------------------')
print('Imprimindo a Tabuada (de 0 a 10) do número {}'.format(x))
print('-------------------------------------------')

print('{}x0 = {}'.format(x, x * 0))
print('{}x1 = {}'.format(x, x * 1))
print('{}x2 = {}'.format(x, x * 2))
print('{}x3 = {}'.format(x, x * 3))
print('{}x4 = {}'.format(x, x * 4))
print('{}x5 = {}'.format(x, x * 5))
print('{}x6 = {}'.format(x, x * 6))
print('{}x7 = {}'.format(x, x * 7))
print('{}x8 = {}'.format(x, x * 8))
print('{}x9 = {}'.format(x, x * 9))
print('{}x10 = {}'.format(x, x * 10))

#  Esse programa provavelmente vai utilizar um laço de repetição posteriormente

'''
Edit: é possível usar 
    print('-' * 15)
em vez de print('-------')
'''
