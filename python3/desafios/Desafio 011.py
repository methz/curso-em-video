print('\nDesafio relacionado ao curso de Python do Curso em Vídeo')
print('------------------------------------------------------------')
print('Autor: Marcos Oliveira')
print('Desafio: 011')
print('Aula: Curso Python #07 - Operadores Aritméticos')
print('------------------------------------------------------------')
print('Carregando o programa...')
print('Programa iniciado com sucesso')
print('------------------------------------------------------------')

b = float(input('Digite a largura da parede (em metro): '))
h = float(input('Digite a altura da parede (em metro): '))

area = b * h  # Considerando uma parede retangular
tinta = 2

print('A área de uma parede {}x{} é igual a {} m².'.format(b, h, area))
print('Considerando que cada litro de tinta pinta {} m², será necessário {} litro(s) de tinta.'. format(tinta, area/tinta))