class Conta:
  pass

  def __init__(self, numero, titular, limite, saldo=0):
    print("Construindo o objeto ...{}".format(self))
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite
    self.__tarifa_transferencia = 8.0
    self.__codigo_banco ='001'

  def extrato(self):
    print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

  def deposita(self, valor):
    self.__saldo += valor

  def saca(self, valor):
    if(self.__pode_sacar(valor)):
      self.__saldo -= valor
      return True
    else:
      print("O valor {} ultrapassou o limite".format(valor))
      return False

  def transfere(self, valor, conta_destino):
    valor_saque = valor + self.__tarifa_transferencia
    if(self.saca(valor_saque)):
      conta_destino.deposita(valor)
      print("Transferencia Efetuada")

  @property
  def saldo(self):
    return self.__saldo

  def get_titular(self):
    return self.__titular

  @property
  def limite(self):
    return self.__limite

  @limite.setter
  def limite(self, novo_limite):
    self.__limite = novo_limite

  def __pode_sacar(self, valor_a_sacar):
    valor_disponivel_a_sacar = self.__saldo + self.__limite
    return valor_a_sacar<= valor_disponivel_a_sacar

  @staticmethod
  def codigo_banco():
    return "001"

  @staticmethod
  def codigo_bancos():
    return {"BB": "001", "Caixa": "104", "Inter": "077"}

