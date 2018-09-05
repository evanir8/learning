# exercicios de exemplo do curso de ruby oop da alura
#
require_relative 'estoque'
require_relative 'produto'
require_relative 'impresso'

class Livro < Produto
  attr_reader :possui_sobrecapa, :possui_reimpressao

  include Impresso

  def initialize(titulo, preco, ano_lancamento, possui_reimpressao, editora, possui_sobrecapa = false)
    super(titulo, preco, ano_lancamento, editora)
    @possui_reimpressao = possui_reimpressao
    @possui_sobrecapa = possui_sobrecapa
  end

  def matches?(query)
    %w[livro impresso].include? query
  end
end
