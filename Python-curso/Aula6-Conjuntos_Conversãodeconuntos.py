conjunto = {1, 2, 3, 4, 5}  # O conjunto exibe apenas 1 de cada elemento, ou seja, se adicionar um outro 3 na lista, ao dar um "Print" ele não será exibido
conjunto2 = {5, 6, 7, 8}

conjunto_mescaldo = conjunto.union(conjunto2) #O ".union" junta os dois conjuntos em 1 só e o tipo "Lista" organiza eles em ordem

conjunto_interseccao = conjunto.intersection(conjunto2) #O conjunto interseccao mostra todos os numeros que estão repetidos dentro do conjunto

conjunto_diferenca = conjunto.difference(conjunto2) # Ele mostra o que há de diferente entre o conjunto 1 e o conjunto 2

conjunto_diff = conjunto.symmetric_difference(conjunto2) #Caso haja dois conjuntos parecidos, ele informa o que há de diferente entre os dois, ex: caso tenha dois conjuntos, um com 123 e outro com 1234, ele informará apenas 4

conjunto_a = {1, 2, 3,}
conjunto_b = {1, 2, 3, 4}
conjunto_subset = conjunto_a.issubset(conjunto_b) #Ele irá mostrar se o valor do conjunto "Se enquandra" dentro do outro conjunto, também tem o "issuperset" que faz o contrario

lista = ['cachorro', 'gato', 'gato', 'elefante']
print('A lista atual está dessa forma: {}' .format(lista))

lista_semduplicidade = set(lista) #O comando "set" converte a lista para conjunto, por isso remove a duplicidade
print('A lista após a conversão para conjunto está dessa forma: {}' .format(lista_semduplicidade))

lista_convertida = list(lista_semduplicidade)
print('A lista após a conversão para lista novamente está dessa forma: {}' .format(lista_convertida))

print('União: {}' .format(conjunto_mescaldo))
print('Intersecção: {}' .format(conjunto_interseccao))
print('Diferença: {}' .format(conjunto_diferenca))
print('Diferença simetrica: {}' .format(conjunto_diff))
print('O conjunto "A" é subconjunto do "B": {}' .format(conjunto_subset))


# conjunto.add(6)   # Para os dois comandos a seguir, o "add" adiciona um numero novo ao junto, e o "discard" remove um numero do conjunto
# conjunto.discard(1)