$LOAD_PATH << '.'
require 'impostos.rb'
require 'orcamento.rb'

class CalculadorDeImpostos
  # include impostos::ICMS

  def realiza_calculo(orcamento, imposto)
    imposto_calculado = imposto.calcula(orcamento)
    puts imposto_calculado
  end
end

calculador = CalculadorDeImpostos.new
orcamento = Orcamento.new
orcamento.adiciona_item(Item.new('ITEM 1', 50))
orcamento.adiciona_item(Item.new('ITEM 2', 200))
orcamento.adiciona_item(Item.new('ITEM 3', 250))

puts 'ISS'
calculador.realiza_calculo(orcamento, ISS.new)
puts 'ICMS'
calculador.realiza_calculo(orcamento, ICMS.new)
puts 'ISS com ICMS'
calculador.realiza_calculo(orcamento, ISS.new(ICMS.new))
puts 'ICPP'
calculador.realiza_calculo(orcamento, ICPP.new)
puts 'IKCV'
calculador.realiza_calculo(orcamento, IKCV.new)
puts 'ICPP + IKCV'
calculador.realiza_calculo(orcamento, ICPP.new(IKCV.new))
