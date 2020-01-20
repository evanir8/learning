print("**********************************")
print("Bem vindo ao jogo de  Adivinhação!")
print("**********************************")

import random

total_de_tentativas =random.randrange(1,101)
rodada = 1
# while (rodada <=  total_de_tentativas):
for rodada in range(1, total_de_tentativas):
    print("Tentativa  {} de {}".format(rodada, total_de_tentativas))
    chute = int(input("Digite o seu numero:"))

    print("Voce digitou ", chute)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Voce Acertou")
        rodada = 4
    else:
        if(maior):
            print("Voce Errou, seu chute foi maior que o numero secreto!")
        elif(menor):
            print("Voce Errou, seu chute foi menor que o numero secreto!")
rodada += 1

print("Tente outra vez!")

print("Fim do Jogo")
