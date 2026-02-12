print("Seja muito bem vindo ao quiz do João!")
answer_user = input("Quer começar? (S/N) ")

if answer_user != "S":
    quit()

score = 0

print("Começando...")

print("Quem desenvolveu o jogo Grand Theft auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correcto!")
    score = score + 1
else:
    print("Incorreto!")

print("Quem quem foi o protagonista do jogo GTA San Andres? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correcto!")
    score = score + 1
else:
    print("Incorreto!")

print(f"Quiz acabou... Pontuação: {score}/2")