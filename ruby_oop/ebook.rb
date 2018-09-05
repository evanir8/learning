require_relative 'estoque'
require_relative 'produto'
class Ebook < Produto

  # include Produto

  def matches?(query)
    %w[ebook digital].include? query
  end

end
