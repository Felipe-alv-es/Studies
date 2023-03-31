contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'rato']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b

print(soma(10, 20))

calculadora = {
    'soma': lambda a,b: a + b,
    'subtracao': lambda a,b: a - b,
    'divisao': lambda a,b: a / b,
    'multiplicacao': lambda a,b: a * b,
}

soma = calculadora['soma']
sub = calculadora['subtracao']
div = calculadora['divisao']
mult = calculadora['multiplicacao']

print(soma(50, 50))
print(div(50, 50))
