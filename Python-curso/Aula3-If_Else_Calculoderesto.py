a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > 10 or b > 10 or c > 10:
    print('Insira um valor abaixo de 10')
else:
    if a > b and a > c:
        print('O maior valor é: {}'.format(a))
        impopar = a
    elif b > a and b > c:
        print('O maior valor é: {}'.format(b))
        impopar = c
    else:
        print('O maior valor é: {}'.format(c))
        impopar = c

    if impopar % 2:
        print('O numero informado é impar')
    else:
        print('O numero informado é par')

print('Fim do calculo')

