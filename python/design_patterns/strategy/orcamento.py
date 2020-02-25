class Orcamento(object):
    def __init__(self, valor):
        self.__valor = valor
        self.__impostos = impostos.split(",")

    @property
    def valor(self):
        return self.__valor

