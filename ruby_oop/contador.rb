module Contador
  def << (livro)
    push (livro)
    if @maximo_necessario.nil? || @maximo_necessario < size
      @maximo_necessario = size
    end
    self
  end

  def maximo_necessario
    @maximo_necessario
  end

  attr_reader :maximo_necessario
end


class Float
  def to_dinheiro
    str << 'R$ ' + self.to_s.gsub('.', ',')
    str << "0" unless str.match /(.*)(\d{2})$/
    valor
  end
end

class Conversor
  def initialize(str)
    @str = str
  end

  def string_para_alfanumerico
    @str = @str.gsub(/[^\w\s]/, '')
    puts @str
  end
end
