import random

print("\t\t-=-"*4)
print("\t\t-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("")
print("O jogo é simples chute um número de 1 a 50. Você terá 20 tentativas. ")
print("")
print("\t\t\t-----?PRONTO?-----")
print("")

N1=random.randrange(1,50)
chances=20
chute=0

while chute!=random:

    chute=int(input("Digite um número entre 1 a 50: "))
    if chute:
        chute = int(chute)
        chances = chances - 1

    if chances==0:
        print("Suas chances acabaram!")
        break
    if chute<1 or chute>50:
        print("Número inválido. Digite novamente um número entre 1 e 50")
        print("")
        continue

    if chute==N1:
        print("Parabéns você acertou o número!")
        print("")
        break
    else:
        if chute>N1:
            print("Você errou, este número foi maior! tente novamente.")
            print("")
            print(f"Restam {chances} tentativas de 20.")
            print("")
        else:
            print("Você errou, este número foi menor! tente novamente.")
            print("")
            print(f"Restam {chances} tentativas de 20.")
            print("")
print("")
print("")
print("GAME OVER!")