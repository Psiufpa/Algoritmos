# GUSTAVO LARA DA SILVA
# JOGO DA VELHA (TIC-TAC-TOE)


tabuleiro = ["1","2","3","4","5","6","7","8","9"]  # define os índices iniciais do tabuleiro antes de iniciar a jogada 

jogador = "X"   # inicia com o jogador X
jogadas = 0     # contador para contar a quantidade de jogadas
ganhou = False  # variavel sentinela

while jogadas < 9 and ganhou == False:    # condição para seguir rodando o jogo
    print("\n")
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("---------")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("---------")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])

    print("\n")
    posicao = int(input("Jogador " + jogador + ", escolha uma posição para jogar: "))

    if posicao < 1 or posicao > 9:        # valida para jogada de apenas numeros entre 1 e 9  
        print("Posição inválida!")
    else:
        if tabuleiro[posicao - 1] == "X" or tabuleiro[posicao - 1] == "O":  # valida para jogadas já realizadas
            print("Essa posição já foi escolhida!")
        else:
            tabuleiro[posicao - 1] = jogador
            jogadas += 1

            # verifica se houve vitória
            if tabuleiro[0] == tabuleiro[1] and tabuleiro[1] == tabuleiro[2]:
                ganhou = True
            elif tabuleiro[3] == tabuleiro[4] and tabuleiro[4] == tabuleiro[5]:
                ganhou = True
            elif tabuleiro[6] == tabuleiro[7] and tabuleiro[7] == tabuleiro[8]:
                ganhou = True
            elif tabuleiro[0] == tabuleiro[3] and tabuleiro[3] == tabuleiro[6]:
                ganhou = True
            elif tabuleiro[1] == tabuleiro[4] and tabuleiro[4] == tabuleiro[7]:
                ganhou = True
            elif tabuleiro[2] == tabuleiro[5] and tabuleiro[5] == tabuleiro[8]:
                ganhou = True
            elif tabuleiro[0] == tabuleiro[4] and tabuleiro[4] == tabuleiro[8]:
                ganhou = True
            elif tabuleiro[2] == tabuleiro[4] and tabuleiro[4] == tabuleiro[6]:
                ganhou = True

            if ganhou == True:
                print("\n")
                print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
                print("---------")
                print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
                print("---------")
                print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])

                print("\n")
                print("O jogador", jogador, "venceu!")
            else:
                if jogador == "X":
                    jogador = "O"
                else:
                    jogador = "X"

if ganhou == False:
    print("\n")
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("---------")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("---------")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])

    print("\n")
    print("Jogo empatado! Deu velha!")