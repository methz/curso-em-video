import math  # importando a biblioteca math para usar o método da raiz quadrada

print('\nDesafio relacionado ao curso de Python do Curso em Vídeo')
print('------------------------------------------------------------')
print('Autor: Marcos Oliveira')
print('Desafio: 006')
print('Aula: Curso Python #07 - Operadores Aritméticos')
print('------------------------------------------------------------')
print('Carregando o programa...')
print('Programa iniciado com sucesso')
print('------------------------------------------------------------')

number = float(input('Digite um número: \n'))

print('O dobro de {} é igual a {} \n'.format(number, number * 2))
print('O triplo de {} é igual a {} \n'.format(number, number * 3))
print('A raiz quadrada (usando a propriedade inversa de exponenciação) de {} é igual a {:.2f} \n'.format(number, number ** 0.5))
print("A raiz quadrada de {} usando o método 'sqrt' é igual a {:.2f}".format(number, math.sqrt(number)))

'''
Após assistir a resolução do Guanabaraba, coloquei a formatação ":.2f" para imprimir a raiz quadrada.
Não tinha pensado no método 'pow' que o Guanabara apresentou, mas não acho necessário colocá-lo agora.
'''