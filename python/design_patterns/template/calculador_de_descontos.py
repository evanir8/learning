from descontos import Desconto_por_cinco_items, Desconto_por_mais_de_quinhentos_reais

class Calculador_de_descontos(object):

    def calcula(self, orcamento):
      desconto = Desconto_por_cinco_items().calcula(orcamento)
      if desconto == 0:
        desconto = Desconto_por_mais_de_quinhentos_reais().calcula(orcamento)
      return desconto


if __name__ == '__main__':
  from orcamento import Orcamento, Item

  orcamento = Orcamento()
  orcamento.adiciona_item(Item('Item -1', 120))
  orcamento.adiciona_item(Item('Item -2', 50))
  orcamento.adiciona_item(Item('Item -3', 400))

  print orcamento.valor
  calculador = Calculador_de_descontos()
  desconto_calculado = calculador.calcula(orcamento)
  print "Desconto Calculado: {} ".format(desconto_calculado)

