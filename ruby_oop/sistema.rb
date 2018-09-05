require_relative 'livro'
require_relative 'revista'
require_relative 'ebook'

# require_relative 'estoque'

def livro_para_newsletter(livro)
  if livro.ano_lancamento < 2000
    puts "Newsletter/Liquidação"
    puts livro.titulo
    puts livro.preco
    puts livro.possui_reimpressao?
  end
end

def @livros.maximo_necessario
  @maximo_necessario
end

algoritmos         = Livro.new("Algoritmos", 100, 1998, true, "editora", false)
arquitetura        = Livro.new("Introdução À Arquitetura e Design de Software", 70, 2011, true, "editora",false)
programmer         = Livro.new("The Pragmatic Programmer", 100, 1999, true, "editora")
ruby               = Livro.new("Programming Ruby", 100, 2004, true, "editora")
revistona          = Revista.new("Revista de Ruby", 10, 2012, true, 3, "Revistas")
online_arquitetura = Ebook.new("Introdução a Arquitetura e Design de Software", 50, 2012, "editora")

estoque = Estoque.new

estoque << algoritmos << algoritmos << ruby << programmer << arquitetura << ruby << ruby << revistona << revistona << online_arquitetura

estoque.vende ruby
estoque.vende algoritmos
estoque.vende algoritmos
estoque.vende revistona
estoque.vende online_arquitetura

puts estoque.livro_que_mais_vendeu_por_titulo.titulo
puts estoque.revista_que_mais_vendeu_por_titulo.titulo
puts estoque.ebook_que_mais_vendeu_por_titulo.titulo

puts estoque.respond_to?(:ebook_que_mais_vendeu_por_titulo)

puts algoritmos.calcula_preco(100)
puts revistona.calcula_preco(15)
puts online_arquitetura.calcula_preco(70)
