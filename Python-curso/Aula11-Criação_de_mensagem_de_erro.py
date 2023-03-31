class Error(Exception):
    pass

class InputError(Error):  #Essas duas classes são necessárias para criar uma "Classe de erro"
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print('A nota inserida foi {} ' .format(x))
        if x > 10:
            raise InputError('Insira um valor menor que 10')
        elif x < 0:
            raise InputError('Insira uma nova acima de 0')
        break #O break força a saida do looping criado pelo "while True"
    except ValueError:
        print('Valor invalido. Deve-se digitar apenas números. ')
    except InputError as ex:
        print(ex)