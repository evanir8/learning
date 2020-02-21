$LOAD_PATH << '.'

class CalculadorDeImpostos
  require 'impostos.rb'
  # include impostos::ICMS

  def realiza_calculo(orcamento, imposto)
    imposto_calculado = imposto.calcula(orcamento)
    imposto_calculado
  end
end

require 'orcamento.rb'
calculador = CalculadorDeImpostos.new
orcamento = Orcamento.new(500)
puts calculador
puts orcamento
# calculador.realiza_calculo(orcamento, ISS())
# calculador.realiza_calculo(orcamento, ICMS())
puts 'Testando'
