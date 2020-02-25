class Desconto_por_cinco_items(object):
  def calcula(self, orcamento):
    if orcamento.total_items>5:
      return orcamento.valor * 0.1
    else:
      return 0

class Desconto_por_mais_de_quinhentos_reais(object):
  def calcula(self,orcamento):
    if orcamento.valor > 500:
        return orcamento.valor * 0.07
    else:
        return 0
