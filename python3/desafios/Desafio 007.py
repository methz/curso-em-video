print('\nDesafio relacionado ao curso de Python do Curso em Vídeo')
print('------------------------------------------------------------')
print('Autor: Marcos Oliveira')
print('Desafio: 007')
print('Aula: Curso Python #07 - Operadores Aritméticos')
print('------------------------------------------------------------')
print('Carregando o programa...')
print('Programa iniciado com sucesso')
print('------------------------------------------------------------')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('Sua média artimética é {}'.format((nota1 + nota2)/2))  # forma sem atribuição em variável

# É possível calcular atribuindo a média em uma variável, é mais bonito, talvez.

media = (nota1 + nota2)/2
print('Sua média artimética (com variável) é {}'.format(media))  # forma atribuindo a média numa variável
