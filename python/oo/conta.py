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
