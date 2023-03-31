class Televisao:
    def __init__(self):
        self.ligada = False

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

televisao = Televisao()

if __name__ == '__main__':   #A classe pode ser chamada de fora do arquivo, então esse main serve para que essas funções abaixo sejam executadas só quando o proprio arquivo as chamar

    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)