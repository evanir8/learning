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
  def __init__(self, nome, ano, tmeporadas):
    super().__init__(nome, ano)
    self.tmeporadas = tmeporadas

  def __str__(self):
    return f'{self.nome} - {self.ano} - {self.tmeporadas} tmepo. - {vingadores.likes} likes'

class Playlist:
  def __init__(self, nome, programas):
    self.nome = nome
    self._programas = programas

  def __getitem__(self, item):
    return self._programas[item]

  @property
  def listagem(self):
    return self._programas

  def __len__(self):
    return len(self._programas)



vingadores = Filme('Vingadores - Gerra Infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo Mundo em Panico', 2014, 95)
demolidor = Serie('Demolidor', 2016, 3)
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

for programa in playlist_fim_de_semana.listagem:
  print(programa)
print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')
