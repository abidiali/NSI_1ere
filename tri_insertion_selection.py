def tri_nsertion(liste):
    for index in range(len(liste)): #on parcourt la liste
        item = liste[index]         #un élément de la liste
        j = index
        while j>0 and liste[j-1] > item: #tant qu'on n'a pas atteint le début ou un élément plus petit
            liste[j] = liste[j-1]        #on décale l'élément trouvé vers la droite
            j=j-1
        liste[j]=item       #on insere item a sa place
        
def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab
# Programme principale pour tester le code ci-dessus
tab = [98, 22, 15, 32, 2, 74, 63, 70]
 
print(tri_selection(tab))
 
