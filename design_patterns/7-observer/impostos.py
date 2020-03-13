from abc import ABCMeta, abstractclassmethod

class Imposto(object):
    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calculo_outro_imposto(self, orcamento):
        if self.__outro_imposto is None:
            return 0
        return self.__outro_imposto.calcula(orcamento)

    @abstractclassmethod
    def calcula(self, orcamento):
        pass



class Template_de_imposto_condicional(Imposto):
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) + self.calculo_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) + self.calculo_outro_imposto(orcamento)

    @abstractclassmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractclassmethod
    def maxima_taxacao(self, orcamento):
        pass

    @abstractclassmethod
    def minima_taxacao(self, orcamento):
        pass


class ICPP(Template_de_imposto_condicional):
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

class IKCV(Template_de_imposto_condicional):
    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.01

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_items():
            if (item.valor > 100):
                return True
        return False

#recurso de decorator da linguagem python
# wrapper -> empacotador
# o decorator do Python, exemplo IPVX, sempre vai ser executado
# ao contrario do Decorator implementado, ele pode ser composto conforme a necessidade
def IPVX(metodo_ou_funcao):
    def wrapper(self, orcamento):
        print("Executando o decorator IPVX")
        return metodo_ou_funcao(self, orcamento) + 51
    return wrapper

class ISS(Imposto):
    @IPVX
    def calcula(self, orcamento):
        print("EXECUTANDO o METODO Calcula do ISS")
        return orcamento.valor * 0.1 + self.calculo_outro_imposto(orcamento)


class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_outro_imposto(orcamento)
