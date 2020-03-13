class Orcamento
  attr_reader :valor

  def initialize
    @items = []
  end

  def total
    return @total unless @total.nil?

    @total = 0
    @items.each { |i| @total += i.valor }
    @total
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
