$LOAD_PATH << '.'

class CalculadorDeImpostos
  require 'impostos.rb'
  # include impostos::ICMS

  def realiza_calculo(orcamento, imposto)
    imposto_calculado = imposto.calcula(orcamento)
     puts imposto_calculado
  end
end

require 'orcamento.rb'
calculador = CalculadorDeImpostos.new
orcamento = Orcamento.new(500)
calculador.realiza_calculo(orcamento, ISS.new)
calculador.realiza_calculo(orcamento, ICMS.new)

