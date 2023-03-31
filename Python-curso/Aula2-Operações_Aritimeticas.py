a = 15
b = 20
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

divisao = int(divisao) #Esse codigo está definindo o valor da divisão para "Inteiro"

print('soma: ' + str(soma)) #o "Str" está convertendo o valor inteiro do "Soma" para o formato "String"
print('subtracao: {} ' .format(subtracao))
print('Multiplicacao: {multipli}' .format(multipli=multiplicacao)) #As chaves dentro do print trata-se de um "Alias", onde ele foi buscado pelo "Format" informado
print('Divisão: ' + str(divisao)) #E então está realizando o mesmo que ali acima

a = int(input('Insira um valor aqui: ')) #O valor do input sempre vai ser string, então é necessário converte-lo para a INT para realizar somas

#nomedeusuario = input('Digite seu nome de usuário: ')
#print('Bom dia {username}' .format(username=nomedeusuario))

