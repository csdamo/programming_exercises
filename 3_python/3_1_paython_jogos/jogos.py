import forca
import adivinhacao


def escolhe_jogo():
    print("\033[1;33m*********************************")
    print('****** Escolha o seu jogo! ******')
    print("*********************************\033[m")

    print('(1) Forca (2) Adivinhação')

    jogo = int(input('Qual jogo? '))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhação")
        adivinhacao.jogar()


if __name__ == '__main__':
    escolhe_jogo()
