class Livro
  def initialize(titulo, preco, ano_lancamento, reimpressao)
    @titulo             = titulo
    @ano_lancamento     = ano_lancamento
    @possui_reimpressao = reimpressao
    @preco              = calcula_preco(preco)
  end

  def possui_reimpressao?
    @possui_reimpressao
  end

  def calcula_preco(base)
    puts "\n --- #{possui_reimpressao?} #{@ano_lancamento}"
    multiplicador = if @ano_lancamento < 2006
                       possui_reimpressao? ? 0.9 : 0.95
                    elsif @ano_lancamento <= 2010
                       possui_reimpressao? ? 0.96 : 1
                    else
                       1
                    end
    base * multiplicador
  end
end

arquitetura = Livro.new("Arquitetura de Software", 100, 1999, true)
