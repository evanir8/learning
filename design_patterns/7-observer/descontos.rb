class DescontoPorQuantidade
  def initialize(proximo_desconto)
    @proximo_desconto = proximo_desconto
  end

  def calcula(orcamento)
    puts "Quantidade #{orcamento.qtd_items}"
    if orcamento.qtd_items > 5
      puts 'Aplicando Desconto pela Quantidade'
      (orcamento.total * 0.1).round(2)
    else
      @proximo_desconto.calcula(orcamento)
    end
  end
end

class DescontoPorValor
  def initialize(proximo_desconto)
    @proximo_desconto = proximo_desconto
  end

  def calcula(orcamento)
    puts "Total do Orcamento #{orcamento.total}"
    if orcamento.total > 500
      puts 'Aplicando Desconto pelo Valor'
      (orcamento.total * 0.07).round(2)
    else
      @proximo_desconto.calcula(orcamento)
    end
  end
end

class SemDesconto
  def calcula(_obj)
    0
  end
end
