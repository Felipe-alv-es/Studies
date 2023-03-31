
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')  #O comando open cria um arquivo novo quando executado, caso precise validar se o arquivo existe e edita-lo, ao invés do "w" precisa usar o "a"
    arquivo.write(texto)
    arquivo.close() #Sem ao final, o ideal é fechar o arquivo

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    aluno_nota = aluno_nota.split('\n') #O split faz com que, a partir do ponto definido, ele "corta" e cria uma lista, no caso do exemplo, sempre que encontrar um \n ele fará o split
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        lista_media.append({aluno:media(lista_notas)})
    return lista_media
        #print(media(lista_notas))

def copia_arquivo(nome_arquivo):
    import shutil  #Através desse comando, será importado a biblioteca shutil para copiar o arquivo, o ideal é sempre importar o modulo no topo do arquivo, assim qualquer modulo pode utiliza-lo
    #shutil.copy(nome_arquivo, 'Caminho do diretório') Esse comando copiará o arquivo para determinado diretório

def move_arquivo(nome_arquivo):
    import shutil
    #shutil.move(nome_arquivo, 'Caminho do diretório')

if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)
    #escrever_arquivo('Primeira linha. \n')
    #aluno = 'Rafael,10,10,5,5\n'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('teste.txt')