# le système de monnaie disponible
valeurs = [50, 100, 200, 500, 1000,5000]
 
def rendu_de_monnaie(somme_a_payer, somme_versee):
    liste = []
    a_rendre = somme_versee - somme_a_payer
    # par exemple 8 €
 
    # indice « tout à droite »
    indice = len(valeurs) - 1
 
    while a_rendre > 0: # on sort quand tout payé
        piece = valeurs[indice]
        # Soit la pièce est trop grande
        if piece > a_rendre:
            # on regardera une piece plus petite
            indice -= 1
        # soit on la rend (on rembourse)
        else:
            # on l'ajoute à la liste
            liste.append(piece)
            # on la soustrait de la somme à rendre
            a_rendre -= piece
    # on renvoie la liste
    return liste
 
# demandes à l'utilisateur 
somme_a_payer = int(input("Somme à payer ? : "))
# exemple 42 €
somme_versee = int(input("Somme versée ? : "))
# exemple 50 €
 
# Affichage des pièces et billets à rendre
liste_de_pieces = rendu_de_monnaie(somme_a_payer, somme_versee)
print(liste_de_pieces)