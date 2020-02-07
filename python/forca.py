
import random


def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de  Adivinhação!")
    print("**********************************")

    palavras = []
    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    # arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    # palavra_secreta = "demotilamonofamila".upper()
    # letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = input("Qual letra? ").strip().upper()
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            print("{} beeen".format(chute))
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        # palavra_secreta.find(chute)
        print(letras_acertadas)
    if(acertou):
        print("Parabéns você acertou!")
    else:
        print("Você perdeu, tente novamente!")
    print("Fim do Jogo")


if(__name__ == '__main__'):
    jogar()
