$LOAD_PATH << '.'
require 'descontos.rb'
require 'orcamento.rb'

class CalculadorDeDescontos
  def calcula(orcamento)
    DescontoPorQuantidade.new(DescontoPorValor.new(SemDesconto.new)).calcula(orcamento)
  end
end

orcamento = Orcamento.new
orcamento.adiciona_item(Item.new('teste em Ruby', 100))
orcamento.adiciona_item(Item.new('teste em Ruby 2', 100))
orcamento.adiciona_item(Item.new('teste em Ruby 4', 100))
orcamento.adiciona_item(Item.new('teste em Ruby 3', 100))
orcamento.adiciona_item(Item.new('teste em Ruby 6', 250))
# orcamento.adiciona_item(Item.new('teste em Ruby 7', 10))
# orcamento.adiciona_item(Item.new('teste em Ruby 10', 100))

puts orcamento.valor
calculador = CalculadorDeDescontos.new
desconto = calculador.calcula(orcamento)
puts " Desconto Concedido #{desconto}"
