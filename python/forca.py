
import random


def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de  Adivinhação!")
    print("**********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    while(not enforcou and not acertou):
        chute = input("Qual letra? ").strip().upper()
        index = 0
        for letra in palavra_secreta:
            if(chute == letra.upper()):
                letras_acertadas[index] = letra
            index += 1
        palavra_secreta.find(chute)
        print(letras_acertadas)
    print("Fim do Jogo")


if(__name__ == '__main__'):
    jogar()
