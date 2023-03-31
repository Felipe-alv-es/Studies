
lista = [1, 10]
arquivo = open('teste.txt', 'r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print('Não é possível realizar divisão por 0')
except IndexError:
    print('Erro ao acessar um indice desconhecido')
except BaseException as ex:
    print('erro desconhecido. Erro: {}' .format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa, independente do que foi executado acima')