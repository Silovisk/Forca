import random
from palavras import palavras
import string


def pegar_palavra_valida():
    palavra = random.choice(palavras)
    while '-' in palavra or ' ' in palavra:  # Enquanto a palavra contiver hi-fem ou espaço vai randomizar outra palavra
        palavra = random.choice(palavras)
    return palavra.strip().upper()  # retorna palavra sem espaços e maiuscula


def desenhar_boneco(vidas):
    reset_color = "\033[0m"
    red_color = "\033[1;31m"
    yellow_color = "\033[1;36m"

    if vidas == 6:
        return f"""
         {yellow_color}╔═══╗{reset_color}
         {yellow_color}║   O{reset_color}
         {yellow_color}║{reset_color}     
         {yellow_color}║{reset_color}    
         {yellow_color}║{reset_color}    
         {yellow_color}║{reset_color}    
        {red_color}═══════════{reset_color}"""
    elif vidas == 5:
        return f"""
         {yellow_color}╔═══╗{reset_color}
         {yellow_color}║   O{reset_color}
         {yellow_color}║   |{reset_color}     
         {yellow_color}║{reset_color}    
         {yellow_color}║{reset_color}    
         {yellow_color}║{reset_color}    
        {red_color}═══════════{reset_color}"""
    elif vidas == 4:
        return f"""
         {yellow_color}╔═══╗{reset_color}
         {yellow_color}║   O{reset_color}
         {yellow_color}║  /|{reset_color}     
         {yellow_color}║{reset_color}    
         {yellow_color}║{reset_color}    
         {yellow_color}║{reset_color}    
        {red_color}═══════════{reset_color}"""
    elif vidas == 3:
        return f"""
         {yellow_color}╔═══╗{reset_color}
         {yellow_color}║   O{reset_color}
         {yellow_color}║  /|\\{reset_color}     
         {yellow_color}║{reset_color}    
         {yellow_color}║{reset_color}    
         {yellow_color}║{reset_color}    
        {red_color}═══════════{reset_color}"""
    elif vidas == 2:
        return f"""
         {yellow_color}╔═══╗{reset_color}
         {yellow_color}║   O{reset_color}
         {yellow_color}║  /|\\{reset_color}     
         {yellow_color}║  / {reset_color}  
         {yellow_color}║{reset_color}    
         {yellow_color}║{reset_color}    
        {red_color}═══════════{reset_color}"""
    elif vidas == 1:
        return f"""
         {yellow_color}╔═══╗{reset_color}
         {yellow_color}║   O{reset_color}
         {yellow_color}║  /|\\{reset_color}     
         {yellow_color}║  / \\{reset_color}  
         {yellow_color}║{reset_color}    
         {yellow_color}║{reset_color}    
        {red_color}═══════════{reset_color}"""
    else:
        return f"""
         {red_color}╔═══╗{reset_color}
         {red_color}║   X{reset_color}
         {red_color}║  /|\\{reset_color}     
         {red_color}║  / \\{reset_color}  
         {red_color}║{reset_color}    
         {red_color}║{reset_color}    
        {red_color}═══════════{reset_color}"""


def desenhar_trofeu(tamanho):
    print('\033[91m       ___\033[0m' * tamanho)
    print('\033[93m   _.-\'\033[0m\033[92m_\033[0m\033[93m`._\033[0m' * tamanho)
    print('\033[94m  |\033[0m\033[95m  _|_\033[0m\033[94m  |\033[0m' * tamanho)
    print('\033[96m  |\033[0m\033[92m |\033[0m\033[96m  |  |\033[0m' * tamanho)
    print('\033[93m  |\033[0m\033[91m |\033[0m\033[93m  |  |\033[0m' * tamanho)
    print('\033[92m   `\\\033[0m\033[96m  |  |\033[0m' * tamanho)
    print('\033[91m     `\\\033[0m\033[93m|\033[0m\033[91m  |  |\033[0m' * tamanho)
    print('\033[95m       |  |\033[0m' * tamanho)
    print('\033[94m       |  |\033[0m' * tamanho)
    print('\033[96m       |  |\033[0m' * tamanho)
    print('\033[92m       |  |\033[0m' * tamanho)
    print('\033[93m       |  |\033[0m' * tamanho)
    print('\033[95m       |  |\033[0m' * tamanho)
    print('\033[91m       |  |\033[0m' * tamanho)
    print('\033[94m       |  |\033[0m' * tamanho)
    print('\033[96m       |  |\033[0m' * tamanho)
    print('\033[92m       |  |\033[0m' * tamanho)
    print('\033[93m       |  |\033[0m' * tamanho)
    print('\033[95m      /|\033[0m\033[94m  |\033[0m\033[95m\\\033[0m' * tamanho)
    print('\033[91m     / |\033[0m\033[96m  |\033[0m\033[91m \\\033[0m' * tamanho)
    print('\033[94m    /__|\033[0m\033[95m  |__\\\033[0m' * tamanho)
    print('\033[96m   /`  |\033[0m\033[92m  |  `\\\033[0m' * tamanho)
    print('\033[92m  /    |\033[0m\033[93m  |    \\\033[0m' * tamanho)
    print('\033[95m |_____|\033[0m\033[94m  |_____|\033[0m' * tamanho)


def forca():
    # chama a função para pegar uma palavra valida
    palavra = pegar_palavra_valida()
    # cria um conjunto com as letras da palavra
    letras_da_palavra = set(palavra)
    # cria um conjunto com todas as letras do alfabeto em caixa alta
    alfabeto = set(string.ascii_uppercase)
    # cria um conjunto vazio para armazenar as letras usadas pelo jogador
    letras_usadas = set()

    # define a quantidade de vidas do jogador
    vidas = 6
    # desenha o boneco inicial na tela
    print(desenhar_boneco(vidas))
    # enquanto houver letras na palavra para adivinhar e o jogador ainda tiver vidas
    while len(letras_da_palavra) > 0 and vidas > 0:
        # exibe as letras adivinhadas até agora e as letras ja usadas
        print(f"\nVoce tem {vidas} vidas\nVoce usou essa letras:  {' '.join(letras_usadas)}")

        # cria uma lista com as letras da palavra ou '_' se a letra ainda não foi adivinhada
        lista_palavras = [letra if letra in letras_usadas else '_' for letra in palavra]
        # exibe a lista de letras adivinhadas até agora
        print(f"Palavra atual: \n{' '.join(lista_palavras)}")

        # solicita uma letra ao jogador
        letra_jogador = str(input("Adivinhe a letra: ")).strip().upper()

        # verifica se a letra é uma letra valida que ainda não foi usada pelo jogador
        if letra_jogador in alfabeto - letras_usadas:
            # adiciona a letra ao conjunto de letras usadas pelo jogador
            letras_usadas.add(letra_jogador)

            # se a letra adivinhada estiver na palavra
            if letra_jogador in letras_da_palavra:
                # remove a letra do conjunto de letras da palavra
                letras_da_palavra.remove(letra_jogador)

            # se a letra adivinhada não estiver na palavra
            else:
                # o jogador perde uma vida e é exibido o boneco atualizado
                vidas -= 1
                print(f"\033[1;31;40m Letra {letra_jogador} nao existe na palavra \033[m")
                print(desenhar_boneco(vidas))

        # se o jogador ja tiver usado essa letra
        elif letra_jogador in letras_usadas:
            print("\033[1;31;40m Voce ja usou essa letra \033[m")

        # se a letra não for uma letra valida
        else:
            print("\033[1;31;40m Caractere invalido \033[m")

    # se o jogador tiver perdido todas as vidas
    if vidas == 0:
        print(f"\033[1;31;40m Voce morreu e a palavras era: {palavra} \033[m")

    # se o jogador tiver adivinhado todas as letras da palavra
    else:
        print(f"\033[1;32;40mVoce adivinhou a palavra {palavra}!! ")
        print(f"Voce ganhou {vidas} Troféus \033[m")
        desenhar_trofeu(vidas)


# chama a função principal para iniciar o jogo
forca()
