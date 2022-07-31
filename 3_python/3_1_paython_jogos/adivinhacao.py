import random


def jogar():
    print("\033[1;33m*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\033[m")

    jogar_novamente = True
    pontos = 1000

    while jogar_novamente:

        # DIFICULDADE DO JOGO
        dificuldade = int(input('Qual a dificuldade do jogo: (1) Fácil (2) Médio (3) Difícil'))
        if dificuldade != 1 and dificuldade != 2 and dificuldade != 3:
            print('Digite um número de dificuldade válido')
            continue
        if dificuldade == 1:
            numero_maximo = 11
        elif dificuldade == 2:
            numero_maximo = 21
        else:
            numero_maximo = 31

        # VARIAVEIS PARA O JOGO
        # numero_secreto = int(random.random()*10)
        # outra possibilidade: numero_secreto = round((random.random()*10))
        numero_secreto = random.randrange(1, numero_maximo)
        tentativas = 3
        rodada = 1

        while rodada <= tentativas:
            # com o for, uma tentativa é gasta caso digite o número errado: for rodada in range(1, tentativas + 1):

            print('\nRodada {} de {}\n'.format(rodada, tentativas))

            chute = int(input('Digite o seu número entre 1 e {}: '.format(numero_maximo - 1)))

            if chute < 1 or chute > numero_maximo - 1:
                print('Valor inválido. Informe um número entre 1 e {}: '.format(numero_maximo - 1))
                continue

            acertou = chute == numero_secreto
            maior = chute > numero_secreto

            if acertou:
                pontos += 200 * dificuldade
                print('\033[1;30;41mVocê acertou! Você fez {}\033[m'.format(pontos))
                break
            pontos_perdidos = abs((numero_secreto - chute)*rodada*dificuldade)
            if rodada < 3:

                if maior:
                    print('Você errou. O número secreto é menor que {}'.format(chute, pontos_perdidos))
                    pontos -= pontos_perdidos
                else:
                    print('Você errou. O número secreto é maior que  {}'.format(chute, pontos_perdidos))
                    pontos -= pontos_perdidos
            else:
                print('\033[1;30;43mVocê errou. O número correto é {}\033[m'.format(numero_secreto, pontos_perdidos))
                pontos -= pontos_perdidos
                print('Você está com {} pontos'.format(pontos))

            rodada += 1

        opcao_jogador = (input('\nVocê quer jogar novamente? (s) Sim ou (n) Não'))

        if opcao_jogador == 'n':
            jogar_novamente = False

    print('Fim do jogo!')


if __name__ == '__main__':
    jogar()
