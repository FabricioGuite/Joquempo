#Jokenpo por Fabrício Pereira e Stephany Ferrão

"""nesse primeira parte foi implementado a escolha do modo de jogo, logo após os
contadores que o programa usa para fazer o placar e para poder entrar e sair do
"while", também a implementação do "random" para o computador fazer as jogadas e
por fim as instruções para mostrar qual número corresponde a qual jogada."""

modo = int(input('''qual será o modo de jogo?

1: jogador vs jogador.
2: jogador vs computador.
3: computador vs computador. '''))

empate = 0
jogador1 = 0
jogador2 = 0
jogarDnv = 0

from random import randint

regra = ('''tesoura = 1
pedra = 2
papel = 3''')

while jogarDnv == 0:

    """aqui já dentro do while que esta boa parte da programação do jogo,
    primeiramente temos a definição do modo de jogo que foi feita acima pelo usuário,
    seja ela: jogador vs jogador, jogador vs computador ou computador vs computador,
    logo após temos a programação das regras do jogo, para dizer quem ganha de quem e
    juntamente a isso já esta a programação para marcar os pontos, por fim temos a
    parte para jogar novamente ou sair."""

    if modo == 1:
        print(regra)
        jogador_1 = int(input("jogador 1, faça sua jogada: "))
        jogador_2 = int(input("jogador 2, faça sua jogada: "))
    elif modo == 2:
        print(regra)
        jogador_1 = int(input("jogador 1, faça sua jogada: "))
        jogador_2 = randint(1 ,3)
        print("o jogador 2 jogou:",jogador_2)

    elif modo == 3:
        print(regra)
        jogador_1 = randint(1 ,3)
        print("o jogador 1 jogou:",jogador_1)
        jogador_2 = randint(1 ,3)
        print("o jogador 2 jogou:",jogador_2)
    else:
        print("jogada inválida")
    if jogador_1 == 1:
        if jogador_2 == 1:
            print("empate")
            empate = empate + 1
        elif jogador_2 == 2:
            print("jogador 2 venceu!")
            jogador2 = jogador2 + 1
        elif jogador_2 == 3:
            print("jogador 1 venceu")
            jogador1 = jogador1 + 1
        else:
            print("jogada inválida")

    elif jogador_1 == 2:
        if jogador_2 == 1:
            print("jagador 1 venceu")
            jogador1 = jogador1 + 1
        elif jogador_2 == 2:
            print("empate")
            empate = empate + 1
        elif jogador_2 == 3:
            print("jogador 2 venceu")
            jogador2 = jogador2 + 1
        else:
            print("jogada inválida")

    elif jogador_1 == 3:
        if jogador_2 == 1:
            print("jogador 2 venceu!")
            jogador2 = jogador2 + 1
        elif jogador_2 == 2:
            print("jogador 1 venceu!")
            jogador1 = jogador1 + 1
        elif jogador_2 == 3:
            print("empate")
            empate = empate + 1
        else:
            print("jogada inválida")

    print("jogador 1:" ,jogador1 ,"//empate:" ,empate, "//jogador 2:" ,jogador2)

    S_ou_N = int(input("jogar novamente? sim = 1, não = 0 : " ))
    if S_ou_N == 0:
        jogarDnv = jogarDnv + 1
# por fim temos a programação para monstrar quem foi o vencedor e também os agradecimentos.

print("jogador 1:" ,jogador1 ,"//empate:" ,empate, "//jogador 2:" ,jogador2)
if jogador1 == jogador2:
 print("a partida terminou empatada")
elif jogador1 > jogador2:
 print("jogador 1 venceu o jogo")
else:
 print("jogador 2 venceu o jogo")
print("obrigado por jogar!!! Um jogo de Fabrício Pereira e Stephany Ferrão")