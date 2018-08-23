# exercicios de exemplo do curso de ruby oop da alura
#
class Livro
  attr_reader :titulo, :ano_lancamento, :preco
  def initialize(titulo, preco, ano_lancamento, possui_reimpressao = false)
    @titulo             = titulo
    @ano_lancamento     = ano_lancamento
    @possui_reimpressao = possui_reimpressao
    @preco              = calcula_preco(preco)
  end

  def possui_reimpressao?
    @possui_reimpressao
  end

  def multiplicador_desconto
    if @ano_lancamento < 2006
      possui_reimpressao? ? 0.9 : 0.95
    elsif @ano_lancamento <= 2010
      possui_reimpressao? ? 0.96 : 1
    else
      1
    end
  end

  def calcula_preco(base)
    base * multiplicador_desconto
  end

  def to_csv
    "#{@titulo}, #{@ano_lancamento}, #{@preco}"
  end
end

class Estoque
  # attr_reader :livros
  def initialize
    @livros = []
  end

  def exporta_csv
    @livros.each do |livro|
      puts livro.to_csv
    end
  end

  def mais_barato_que(valor)
    @livros.select do |livro|
      livro.preco <= valor
    end
  end

  def total
    @livros.size
  end

  def adiciona(livro)
    @livros << livro if livro
  end
end

algoritimos = Livro.new('Algoritimos', 100, 1998, true)
arquitetura = Livro.new('Arquitetura de Software', 70, 2111, true)

estoque = Estoque.new
estoque.adiciona algoritimos
estoque.adiciona arquitetura
estoque.adiciona Livro.new('Tre Pragmatic Programmer', 100, 1999, true)
estoque.adiciona Livro.new('Programming Ruby', 100, 2004, true)

estoque.exporta_csv
puts '----------------------------------------------'
puts "Estoque Total: #{estoque.total} livro(s)"
puts '----------------------------------------------'
puts '---------- Mais baratos que 100,00 -----------'
baratos = estoque.mais_barato_que(80)
baratos.each do |livro|
  puts livro.titulo
end
