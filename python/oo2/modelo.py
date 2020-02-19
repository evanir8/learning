class Filme:
  def __init__(self, nome, ano, duracao):
      self.__nome = nome.title()
      self.ano = ano
      self.duracao = duracao
      self.__likes = 0

  @property
  def likes(self):
    return self.__likes

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, novo_nome):
    self.nome = novo_nome

  @likes.setter
  def likes(self, novo_valor):
    self.likes = novo_valor


class Serie:
  def __init__(self, nome, ano, temporadas):
    self.__nome = nome.title()
    self.ano = ano
    self.temporadas = temporadas
    self.__likes = 0

  def dar_like(self):
    self.__likes += 1

  def unlike(self):
    self.__likes -= 1

  @property
  def likes(self):
    return self.__likes

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, novo_nome):
    self.nome = novo_nome

  @likes.setter
  def likes(self, novo_valor):
    self.likes = novo_valor



vingadores = Filme('Vingadores - Gerra Infinita', 2018, 160)

print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} '
      f'- Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
