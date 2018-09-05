class Produto
  attr_reader :titulo, :ano_lancamento, :preco, :editora

  def initialize(titulo, preco, ano_lancamento, editora)
    @titulo             = titulo
    @ano_lancamento     = ano_lancamento
    @preco              = calcula_preco(preco)
    @editora            = editora
  end

  def calcula_preco(base)
    base * multiplicador_desconto
  end

  def to_csv
    "#{@titulo}, #{@ano_lancamento}, #{@preco}"
  end

  private

  def multiplicador_desconto
    if @ano_lancamento < 2006
      possui_reimpressao? ? 0.9 : 0.95
    elsif @ano_lancamento <= 2010
      possui_reimpressao? ? 0.96 : 1
    else
      1
    end
  end
end
