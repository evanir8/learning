require_relative 'estoque'
require_relative 'produto'

class Revista < Produto
  attr_reader :numero

  # include Produto

  def initialize(titulo, preco, ano_lancamento, possui_reimpressao, numero, editora, possui_sobrecapa = false)
    super(titulo, preco, ano_lancamento, editora)
    @possui_reimpressao = possui_reimpressao
    @numero             = numero
  end

  def matches?(query)
    %w[revista impresso].include? query
  end

  def possui_reimpressao?
    @possui_reimpressao
  end
end
