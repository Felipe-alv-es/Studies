lista = ['Cachorro', 'gato', 'Coelho']
lista.sort()

adicionar = input('Os aniveis da lista são {}, deseja adicionar algum outro? ' .format(lista))

if adicionar == 1:
    lista.append(input('Qual animal deseja realizar a adição? '))
elif adicionar == 2:
    lista.remove(input('Qual animal deseja remover da lista? '))
else:
    print('Não foi digitado nenhuma das opções')

lista.sort()
print('Os animais da lista são {}.' .format(lista))



