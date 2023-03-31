class Calculo:
    def __init__(self, Numa, Numb):
        self.a = Numa
        self.b = Numb

    def soma(self):  #Trata-se de um metodo, onde vc não precisa ficar "re-gerando" o codigo pra realizar essa função
        return self.a + self.b

calculadora = Calculo(10, 20)
print(calculadora.soma())