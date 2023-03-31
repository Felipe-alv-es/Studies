# primo = int(input('Insira um numero: '))
#
# div = 0
#
# for x in range(1, primo+1):
#     resto = primo % x
#     if resto == 0:
# #        print('O numero não é primo ')
#         div = div + 1
#
# if div == 2:
#     print('numero {} é primo' .format(primo))
# else:
#     print('numero {} não é primo' .format(primo))

# for x in range(50, 100):
#     print(x)


###### TODOS NUMEROS PRIMOS ATÈ O NUMERO INFORMADO  #####

valor = int(input('Informe um valor: '))
for num in range(valor+1):

    div = 0

    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div = div + 1

    if div == 2:
        print(num)


###### WHILE NA PRATICA #####


# numero = int(input('Insira um numero acima de 100: '))
#
# while numero <= 100:
#     numero = int(input('O valor informado é abaixo de 100, informe um numero valido: '))
# else:
#     print('Obrigado!')


