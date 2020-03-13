class Orcamento
  attr_reader :valor

  def initialize
    @items = []
  end

  def valor
    return @valor unless @valor.nil?

    @valor = 0
    @items.each { |i| @valor += i.valor }
    @valor
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
