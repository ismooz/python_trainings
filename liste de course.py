import sys

questions = ['Ajouter un élément à la liste', 'Retirer un élément à la liste', 'Afficher la liste', 'Vider la liste', 'Quitter']
lst = []


while True :
    try:
        print("================================================", end="\n")
        print('Choisissez parmi les 5 éléments suivants :')
        for i, element in enumerate(questions):
            print(f'{i + 1}: ', element)
        choix = int(input('Votre choix : '))

        if choix == 1:
            ajout = str(input("Entrez le nom d'un élément à ajouter à la liste de course : "))
            lst.append(ajout.lower().capitalize())
            print(f"L'élément {ajout} a bien été ajouté à la liste.")
            print("================================================", end="\n")
        elif choix == 2:
            retrait = str(input("Entrez le nom d'un élément à retirer à la liste de course : "))
            lst.remove(retrait.lower().capitalize())
            print(f"L'élément {retrait} a bien été retiré à la liste.")
            print("================================================", end="\n")
        elif choix == 3:
            print("============ Votre liste de course =============", end='\n')
            for i, element in enumerate(lst):
                print(f"{i + 1}: ", element)
            print("================================================", end='\n')
        elif choix == 4:
            lst.clear()
            print("La liste a bien été vidée !")
        elif choix == 5:
            sys.exit()
        else:
            print('Merci de bien vouloir choisir avec un nombre de 1 à 5')
       
    except ValueError:
        print('Merci de bien vouloir choisir avec un nombre de 1 à 5')
        
