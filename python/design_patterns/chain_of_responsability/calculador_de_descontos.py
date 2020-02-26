from descontos import Desconto_por_cinco_items, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_descontos(object):

    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_items(
            Desconto_por_mais_de_quinhentos_reais(Sem_desconto)).calcula(orcamento)
        return desconto


if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item -1', 100))
    orcamento.adiciona_item(Item('Item -2', 400))
    orcamento.adiciona_item(Item('Item -3', 150))
    orcamento.adiciona_item(Item('Item -4', 250))
    orcamento.adiciona_item(Item('Item -5', 350))
    orcamento.adiciona_item(Item('Item -6', 250))
    orcamento.adiciona_item(Item('Item -7', 400))

    print(orcamento.valor)
    calculador = Calculador_de_descontos()
    desconto_calculado = calculador.calcula(orcamento)
    print("Desconto Calculado: %s " % desconto_calculado)
