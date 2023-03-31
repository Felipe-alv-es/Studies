lista = [1, 3, 5, 7]
lista_animal = ['cachorro', 'gato', 'rato']

print('A soma dos valores da lista é: {}' .format(sum(lista))) # o sum soma os valores da list
print('O valor mais alto da lista é: {}' .format(max(lista))) # o Max mostra o maior valor, e o min mostra o menor

if 'gato' in lista_animal:
    print('Sim, há um gato na lista')
else:
    print('Não há gato na lista')

listamultiplicada = lista_animal * 3
print('lista multiplicada: {}' .format(listamultiplicada))

listamultiplicada.append(input('Adicione um animal dentro da lista: '))  # O comando "append" adiciona um novo item na lista, o "pop" retira o ultimo item da lista
print('lista multiplicada: {}' .format(listamultiplicada))

tupla = (1, 2, 3, 4,) # A tupla é igual a lista, porem é fixa, não pode ser alterada 

# O comando ".sort" organiza a lista, exemplo "lista.sort()"
