#from impostos import calcula_ISS, calcula_ICMS
from impostos import ISS, ICMS


class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':
    from orcamento import Orcamento, Item

    from impostos import ISS, ICMS, ICPP, IKCV

    orcamento = Orcamento()
    # adicionando itens ao orçamento
    orcamento.adiciona_item(Item('ITEM 1', 50))
    orcamento.adiciona_item(Item('ITEM 2', 200))
    orcamento.adiciona_item(Item('ITEM 3', 250))

    calculador_de_impostos = Calculador_de_impostos()
    print('ISS e ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS())
    calculador_de_impostos.realiza_calculo(orcamento, ICMS())

    print('ISS com ICMS')
    calculador_de_impostos.realiza_calculo(orcamento, ISS(ICMS()))
    # cálculo dos novos impostos
    print('ICPP e IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP())  # imprime 25.0
    calculador_de_impostos.realiza_calculo(orcamento, IKCV())  # imprime 30.0

    print('ICPP com IKCV')
    calculador_de_impostos.realiza_calculo(orcamento, ICPP(IKCV()))  # imprime 25.0
