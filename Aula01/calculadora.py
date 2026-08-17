# Para comentários de varias linhas usamos ''' '''
'''
 Aqui é um comentário de várias linhas.
 Isto também é chamado de DocString
 O que vamos fazer, uma calculadora simples:
 - Pedimos o primeiro numero
 - Pedimos o segundo numero
 - Pedimos o operador
 - Mostramos o resultado
'''
# Para escrever na tela pode usar a ' ou "
print('**********Calculadora**********')
# agora vamos usar uma variavel para armazenar algo na memoria RAM
# Variavel tem um nome e recebe um valor
#nome da variavel, sempre começando com letra, até 30 caracteres
# pode usar numeros e alguns simbolos
# Python faz distinção de maiusculo e minusculo
# nomenclatura de nomes:
#camelCase, Pasalcase, snake_case, kebab-case, lowercase, UPPERCASE
# primeiroNumero = 1 
# PrimeiroNumero = 1
# primeiro_numero = 1
# primeiro-numero = 1
# primeironumero = 1
# PRIMEIRONUMERO = 1
primeiro_numero = input("informe o primeiro numero: ")
segundo_numero = input("informe o segundo numero: ")
operador = input("informe o tipo de calculo '+ - * /' ")
# Tomada de decisão
# Para tomar decisão usamos o if
# Para comparar igualdade use ==
if operador == '+':
    resultado = float(primeiro_numero) + float(segundo_numero)
elif operador == '_':
    resultado = float(primeiro_numero) - float(segundo_numero)
elif operador == '*':
    resultado = float(primeiro_numero) * float(segundo_numero)
elif operador == '/':
    resultado = float(primeiro_numero) / float(segundo_numero)
else:
    resultado = 0
    print("Você informou um operador que não existe!!!")
print(resultado)

