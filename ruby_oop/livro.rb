# exercicios de exemplo do curso de ruby oop da alura
#
require_relative 'estoque'
require_relative 'produto'

class Livro
  attr_reader :possui_sobrecapa, :possui_reimpressao

  include Produto

  def initialize(titulo, preco, ano_lancamento, possui_reimpressao = false, editora, possui_sobrecapa)
    @titulo             = titulo
    @ano_lancamento     = ano_lancamento
    @possui_reimpressao = possui_reimpressao
    @preco              = calcula_preco(preco)
    @editora            = editora
    @possui_sobrecapa   = possui_sobrecapa
  end

  def matches?(query)
    %w[livro impresso].include? query
  end

  def possui_reimpressao?
    @possui_reimpressao
  end
end
