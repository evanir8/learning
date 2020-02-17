class Conta:

  pass

  def __init__(self, numero, titular, limite, saldo=0):
    print("Construindo o objeto ...{}".format(self))
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite

  def extrato(self):
    print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

  def deposita(self, valor):
    self.__saldo += valor

  def saca(self, valor):
    self.__saldo -= valor

  def transfere(self, valor, conta_destino):
    self.saca(valor)
    conta_Destino.deposita(valor)

  def get_saldo(self)
    return self.__saldo

  def get_titular(self)
    return self.__titular

  @property
  def limite(self)
    return self.__limite

  @limite.setter
  def limite(self, novo_limite)
    self.__limite = novo_limite
