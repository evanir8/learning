import random


def jogar():
    print("**********************************")
    print("Bem vindo ao jogo de  Adivinhação!")
    print("**********************************")


    total_de_tentativas = 0
    numero_secreto = random.randrange(1, 101)
    rodada = 1

    print("Qual o numero de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível:"))
    if nivel>3: nivel = 3
    a_tentativas = [20, 10, 5]

    total_de_tentativas = a_tentativas[nivel-1]

    # while (rodada <=  total_de_tentativas):
    for rodada in range(1, total_de_tentativas):
        print("Tentativa  {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite o seu numero:"))

        print("Voce digitou ", chute)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        pontos = 1000

        if(acertou):
            print("Voce Acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Voce Errou, seu chute foi maior que o numero secreto!")
            elif(menor):
                print("Voce Errou, seu chute foi menor que o numero secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
    rodada += 1
    if (rodada== total_de_tentativas):
        print("O numero secreto era {}. voce fez {} pontos".format(numero_secreto, pontos))
    print("Tente outra vez!")

    print("Fim do Jogo")

if(__name__ == '__main__'):
    jogar()
