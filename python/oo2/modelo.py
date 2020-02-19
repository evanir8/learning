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

class Serie(Programa):
  def __init__(self, nome, ano, temporadas):
    super().__init__(nome, ano)
    self.temporadas = temporadas

vingadores = Filme('Vingadores - Gerra Infinita', 2018, 160)

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} '
      f'- Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
