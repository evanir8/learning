class Imposto

  def initialize(outro_imposto = nil)
    @outro_imposto = outro_imposto
  end

  def calculo_outro_imposto(orcamento)
    return 0 unless @outro_imposto

    @outro_imposto.calcula(orcamento)
  end

  def calcula(orcamento)
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end
end


class TemplateDeImpostoCondicional < Imposto
  def calcula(orcamento)
    (deve_usar_maxima_taxacao(orcamento) ? maxima_taxacao(orcamento) : minima_taxacao(orcamento) ) + calculo_outro_imposto(orcamento)

  end

  def deve_usar_maxima_taxacao(_orcamento)
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end

  def maxima_taxacao(_orcamento)
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end

  def minima_taxacao(_orcamento)
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end
end

class ICPP < TemplateDeImpostoCondicional
  def deve_usar_maxima_taxacao(orcamento)
    orcamento.valor > 500
  end

  def maxima_taxacao(orcamento)
    orcamento.valor * 0.07
  end

  def minima_taxacao(orcamento)
    orcamento.valor * 0.05
  end
end

class IKCV < TemplateDeImpostoCondicional
  def deve_usar_maxima_taxacao(orcamento)
    orcamento.valor > 500 && tem_item_maior_que_100_reais(orcamento)
  end

  def maxima_taxacao(orcamento)
    orcamento.valor * 0.1
  end

  def minima_taxacao(orcamento)
    orcamento.valor * 0.06
  end

  private

  def tem_item_maior_que_100_reais(orcamento)
    orcamento.obter_items.each do |item|
      return true if item.valor > 100
    end
    false
  end
end

class ISS < Imposto
  def calcula(orcamento)
    orcamento.valor * 0.1  + calculo_outro_imposto(orcamento)
  end
end

class ICMS < Imposto
  def calcula(orcamento)
    orcamento.valor * 0.06 + calculo_outro_imposto(orcamento)
  end
end
