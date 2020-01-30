
import random


def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de  Adivinhação!")
    print("**********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    while(not enforcou and not acertou):
        chute = input("Qual letra? ").strip().upper()
        index = 0
        for letra in palavra_secreta:
            if(chute == letra.upper()):
                print("Encontrado {} na posicao {}".format(letra, index))
                index += 1
        palavra_secreta.find(chute)
        print("Jogando ...")
    print("Fim do Jogo")


if(__name__ == '__main__'):
    jogar()
