import random

ponto_usuario = 0
ponto_computador = 0
num_partidas = 0

opcoes = ["r", "p", "t"]

while True:

    escolha_usuario = input(
        "escolha r para pedra, p para papel, t para tesoura ou aperte s para sair: ").lower()

    if escolha_usuario == "s":
        break

    if escolha_usuario not in opcoes:
        print("é pra escolher entre as letras r, p, t. Ou se quiser sair aperte s. Vamos começar de novo...")
        continue

    escolha_computador = random.randint(0, 2)
    escolha_computador = opcoes[escolha_computador]

    print(f"o computador esconheu: {escolha_computador}")

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif escolha_usuario == "r" and escolha_computador == "t":
        print("Você ganhou!")
        ponto_usuario = ponto_usuario + 1
    elif escolha_usuario == "p" and escolha_computador == "r":
        print("Você ganhou!")
        ponto_usuario = ponto_usuario + 1
    elif escolha_usuario == "t" and escolha_computador == "r":
        print("Você ganhou!")
        ponto_usuario = ponto_usuario + 1
    else:
        print("Você perdeu!")
        ponto_computador = ponto_computador + 1

    num_partidas = num_partidas + 1

if ponto_usuario > ponto_computador:
    print(
        f"Você venceu! De {num_partidas} você ganhou por {ponto_usuario} X {ponto_computador}. Parabéns!!!")
elif ponto_usuario == ponto_computador:
    print(
        f"Empate! de {num_partidas} partidas o placar final ficou {ponto_usuario} X {ponto_computador}.")
else:
    print(f"Derrota! De {num_partidas} partidas, você perdeu por {ponto_usuario} X {ponto_computador}. Melhor treinar mais pra próxima...")
