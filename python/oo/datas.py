import datetime as dt

class Data:

  def __init__(self, dia, mes, ano):
   self.dia = dia
   self.mes = mes
   self.ano = ano
   self.data_br_format = "{}/{}/{}".format(dia, mes, ano)
   self.date = dt.datetime.strptime(self.data_br_format, '%d/%m/%Y').date()

  def br_formatada(self):
    print(self.data_br_format)
