class Programa:
  def __init__(self, nome, ano):
      self._nome = nome.title()
      self.ano = ano
      self._likes = 0

  @property
  def likes(self):
    return self._likes

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, novo_nome):
    self.nome = novo_nome

  def dar_like(self):
    self._likes += 1

  def unlike(self):
    self._likes -= 1

class Filme(Programa):
  def __init__(self, nome, ano, duracao):
    super().__init__(nome, ano)
    self.duracao = duracao
    self._likes = 0

  def __str__(self):
    return f'{self.nome} - {self.ano} - {self.duracao} min - {vingadores.likes} likes'


class Serie(Programa):
  def __init__(self, nome, ano, temporadas):
    super().__init__(nome, ano)
    self.temporadas = temporadas

  def __str__(self):
    return f'{self.nome} - {self.ano} - {self.temporadas} tempo. - {vingadores.likes} likes'

vingadores = Filme('Vingadores - Gerra Infinita', 2018, 160)


atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
  print(programa)
