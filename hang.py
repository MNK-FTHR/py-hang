import random
import time
import sys
def hang():
    mots = ['CHIEN', 'CHAT', 'OUVRIER', 'PORTE', 'PNEU', 'RADIATEUR', 'GOUVERNEMENT', 'BLANQUETTE']
    life=5
    mot=random.choice(mots)
    # print(mot)
    trys = []
    splited=mot.split()
    guess=mot
    while life >= 0:
        if life == 0:
            print("Vous êtes malheuresement pendu....")
            break
        chose = input("Trouvez une lettre dans le mot: ").upper()
        if chose in trys:
            trys.append(chose)
            life-=1
            print(f'{chose} a déjà été choisi, vous avez perdu une vie, vies restantes:{life}')
        else:
            if chose in mot:
                trys.append(chose)
                print(f'{chose} est dans le mot!')
                verif = []
                for i, w in enumerate(guess):
                    if guess[i] in trys:
                        verif.append(w)
                        sys.stdout.write(w)
                        sys.stdout.flush()
                        time.sleep(0.1)
                    else:
                        sys.stdout.write('_')
                        sys.stdout.flush()
                        time.sleep(0.1)
                print()
                if ''.join(verif) == mot:
                    print("Bravo vous ne serez pas pendu !!!")
                    break

            else:
                life-=1
                print(f'{chose} n\'est pas dans le mot, vous avez perdu une vie, vies restantes:{life}')
hang()