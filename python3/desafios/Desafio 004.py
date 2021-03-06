print('\nDesafio relacionado ao curso de Python do Curso em Vídeo')
print('------------------------------------------------------------')
print('Autor: Marcos Oliveira')
print('Desafio: 004')
print('Aula: Curso Python #06 - Tipos Primitivos e Saída de Dados')
print('------------------------------------------------------------')
print('Carregando o programa...')
print('Programa iniciado com sucesso')
print('------------------------------------------------------------')


x = input('Digite qualquer coisa para análise de tipos: \n')

istype = type(x)
isnumeric = x.isnumeric()
isalpha = x.isalpha()
isalnum = x.isalnum()
isupper = x.isupper()
islower = x.islower()
ispace = x.isspace()
ispress = x.isprintable()

print("-- Analisando a entrada '{}' --".format(x))
print('Identificando o tipo primitivo: {} \n '.format(istype))
print("'{}' é um número? = {}".format(x, isnumeric))
print("'{}' é composto apenas por letras? = {}".format(x, isalpha))
print("'{}' é alfanumérico? = {}".format(x, isalnum))
print("'{}' é um espaço? = {}".format(x, ispace))
print("'{}' está tudo em letras maiúsculas? = {}".format(x, isupper))
print("'{}' está tudo em letras minúsculas? = {}".format(x, islower))
print("'{}' pode ser impresso? = {}".format(x, ispress))

# Problemas detectados:
# - Não aceita o tipo float como 'número'
# - Se usar frases como "oi, eu sou o goku" retorna que não é composto só de letras
