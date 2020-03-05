class Animal
  def reino
    "Animal"
  end

 def vivo?
   true
 end

 def motilidade
   true
 end
end

class Vegetal
 def vivo?
   true
 end

 def motilidade
   false
 end
end

class Mineral
  def vivo?
    false
  end
end

class Mamifero < Animal
  def produz_leite?
    true
  end

  def posse_penas?
    false
  end

  def possue_gueurras?
    false
  end
end

class Ave < Animal
  def produz_leite?
    false
  end

  def possue_gueurras?
    false
  end

  def posse_penas?
    true
  end
end

class Peixe < Animal
  def produz_leite?
    false
  end

  def posse_penas?
    false
  end

  def possue_gueurras?
    true
  end
end

a =  Peixe.new
puts a.vivo?
puts a.reino
puts a.possue_gueurras?
puts a.posse_penas?
puts a.motilidade
