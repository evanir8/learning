class EstadoDeUmOrcamento

  def aplica_desconto_extra(_orcamento)
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end

  def aprova(_orcamento)
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end

  def reprova(_orcamento)
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end

  def finaliza(_orcamento)
    raise NotImplementedError, "#{self.class} has not implemented method '#{__method__}'"
  end
end

class EmAprovacao < EstadoDeUmOrcamento
  def aplica_desconto_extra(orcamento)
    orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
  end

  def aprova(orcamento)
    orcamento.estado_atual = Aprovado.new
  end

  def reprova(orcamento)
    orcamento.estado_atual = Reprovado.new
  end

  def finaliza(orcamento)
    raise Exception, "Orcamento em aprovacao nao pode ser finalizado"
  end

end

class Aprovado < EstadoDeUmOrcamento
  def aplica_desconto_extra(orcamento)
    puts "Aplicando desconto de aprovacao"
    orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
  end

  def aprova(orcamento)
    raise Exception, "Orcamento ja esta aprovado"
  end

  def reprova(orcamento)
    raise Exception, "Orcamento ja esta aprovado"
  end

  def finaliza(orcamento)
    orcamento.estado_atual = Finalizado.new
  end
end

class Reprovado < EstadoDeUmOrcamento
  def aplica_desconto_extra(orcamento)
    raise Exception, "Orcamentos reprovados nao pode ter descontos"
  end

  def aprova(orcamento)
    raise Exception, "Orcamento ja esta Reprovado"
  end

  def reprova(orcamento)
    raise Exception, "Orcamento ja  foi Reprovado"
  end

  def finaliza(orcamento)
    orcamento.estado_atual = Finalizado.new
  end
end

class Finalizado < EstadoDeUmOrcamento
  def aplica_desconto_extra(orcamento)
    raise Exception, "Orcamentos finaçozados nao pode ter descontos"
  end

  def aprova(orcamento)
    raise Exception, "Orcamento ja esta Finalizado"
  end

  def reprova(orcamento)
    raise Exception, "Orcamento ja esta Finalizado"
  end

  def finaliza(orcamento)
    raise Exception, "Orcamento ja esta Finalizadp"
  end
end

class Orcamento
  attr_reader :valor
  attr_accessor :estado_atual

  def initialize
    @items = []
    @estado_atual = EmAprovacao.new
    @desconto_extra = 0
    @descontos_aplicados = []
  end

  def aprova
    self.estado_atual.aprova(self)
  end

  def reprova
    puts "Orcamento Reprovado"
    self.estado_atual.reprova(self)
  end

  def finaliza
    self.estado_atual.finaliza(self)
  end

  def aplica_desconto_extra
    self.estado_atual.aplica_desconto_extra(self)
  end

  def adiciona_desconto_extra(desconto)
    if @descontos_aplicados.include? self.estado_atual
      puts "Ja aplicado desconto extra"
      return
    end
    puts "adicionando desconto #{desconto}"
    @desconto_extra += desconto
    @descontos_aplicados << self.estado_atual
  end

  def valor
    # return @valor unless @valor.nil?

    @valor = 0
    @items.each { |i| @valor += i.valor }
    puts @desconto_extra
    puts "-------------"
    @valor - @desconto_extra
  end

  def qtd_items
    @items.length
  end

  def adiciona_item(item)
    @items << item
  end
end

class Item
  attr_reader :valor

  def initialize(nome, valor)
    @nome  = nome
    @valor = valor
  end
end

orcamento = Orcamento.new
orcamento.adiciona_item(Item.new('Item1',100))
orcamento.adiciona_item(Item.new('Item2',50))
orcamento.adiciona_item(Item.new('Item3',400))

puts orcamento.valor
orcamento.aplica_desconto_extra
puts orcamento.valor

orcamento.aprova
orcamento.aplica_desconto_extra
orcamento.aplica_desconto_extra
puts orcamento.valor
