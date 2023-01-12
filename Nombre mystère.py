import random

myst_num = random.randint(1,100)
essais = 5

print("*** Le jeu du nombre mystère ***")

while essais != 0:
    try:
        print(f"Il te reste {essais} essai{'s' if essais > 1 else ''}")
        player_num = int(input("Devine le nombre mystère entre 1 et 100 : "))
        if player_num > 100:
            essais -= 1
            print("Veuillez entrer un nombre compris entre 1 et 100")
        elif player_num == myst_num:
            essais -= 1
            print(f"Bravo! le nombre mystère est bien le {myst_num}")
            print(f"Tu as trouvée le nombre en {5 - essais} essai{'s' if essais < 4 else ''}")
            print("Fin du jeu.")
            break
        elif player_num > myst_num:
            essais -= 1
            print(f"Le nombre mystère est plus petit que {player_num}")
        else:
            essais -= 1
            print(f"Le nombre mystère est plus grand que {player_num}")
                        
    except:
        print("Veuillez entrer un nombre compris entre 1 et 100")

else:        
    print(f"Dommage ! Le nombre mystère était {myst_num}")
