from aula7parte2 import Televisao  #Esse codigo está importando a função "Televisao" do arquivo "aula7parte2"
from Aula8contador import contador_letras, teste

if __name__ == '__main__':

    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    lista = ['pinguin', 'gato', 'cachorro']
    print(contador_letras(lista))
    print(teste())
