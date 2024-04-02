#Exercice1

mydict={"device":"laptop","constructeur":"acer","ram":"8G","processeur":"intel core i5","stockage":"500G"}
mydict["stockage"]="750"
print(list(mydict.keys()))
print(list(mydict.values()))
print(list(mydict.items()))
mydict["processeur"],mydict["stockage"]=mydict["stockage"],mydict["processeur"]
print(mydict)
mydict["systeme d'exploitation"]= "Windows10"
print(mydict)

#Activité 2
dicT={}
dicPC={"HP": 11 , "Acer": 7 , "Lenovo": 17 , "Del": 23}
dicPhone={"Sumsung": 22 , "Iphone": 9 , "Other": 13 }
dicTablette = {"Sumsung": 15 , "Other": 13}
dicT.update(dicPC)
dicT.update(dicPhone)
dicT.update(dicTablette)
print(dicT)

for d in [dicPC,dicPhone,dicTablette]:
    dicT.update(d)
print(dicT)

#Exercice3
etudiants= {"etudiant_1" : 13 , "etudiant_2" : 17 , "etudiant_3" : 9 , "etudiant_4" : 15 ,"etudiant_5" : 8 , "etudiant_6" : 14 , "etudiant_7" : 16 ,"etudiant_8" : 12 ,"etudiant_9" : 13 , "etudiant_10" : 15 , "etudiant_11" : 14 ,"etudiant_112" : 9 ,"etudiant_13" : 10 , "etudiant_14" : 12 , "etudiant_15" : 13 ,"etudiant_16" : 7 ,"etudiant_17" : 12 , "etudiant_18" : 15 , "etudiant_19" : 9 ,"etudiant_20" : 17 ,}
etudiantAdmis={}
etudiantNonAdmis={}
for key,valeur in etudiants.items():
    if valeur>=10:
        etudiantAdmis[key]= valeur
        print(etudiantAdmis)
    else:
        etudiantNonAdmis[key]=valeur
        print(etudiantNonAdmis)
        
#Exercice4:
D=int(input("donner un entier n"))
L={}
for i in range(0,D+1):
    L.update(i=i*i)
    print(L)

#
C=input("donner une chaine de caractere")
L={}
L.keys()
for i in C:
    if i in L:
        L[]=L[]+1
    else:
        L[]=1
