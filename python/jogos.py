import random
import forca
import adivinhacao


def escolhe_jogo():
  print("**********************************")
  print("**** Esccolha o seu jogo *********''")
  print("**********************************")

  print("(1) Forca (2) Adivinhação")

  jogo = int(input("Escolha o Jogo: "))

  if(jogo == 1):
      print("Jogando Forca")
      forca.jogar()
  elif(jogo == 2):
      print("Jogando Adivinhação")
      adivinhacao.jogar()
  print("Fim do Jogo")

if(__name__ == '__main__'):
  escolhe_jogo()
