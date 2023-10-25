#Exercice 1 :

from random import randint
jour_1=['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
jour_2 = ['samedi', 'dimanche']
 # a faire un classe pour chaque #1,2,3 etc 
#1 

if 'samedi' in jour_1 : 
    print('samedi fait parti de jour_1')
else :
    print('samedi n\'est pas un element de jour_1')

#2
longueur = len(jour_2)
print(f"La longueur de jour_2 est {longueur}")


#3
if jour_1 == jour_2 :
    print('les deux listes sont identiques')
else :
    print('les deux listes sont differentes')


#4
print(f"Le deuxieme element de jour_1 est {jour_1[1]}")

#5
partie14 = jour_1[1:4]
print(f"La partie entre le deuxieme et le quatrieme element de jour_1 est {partie14}")

#6
dimanche_index = jour_2.index("dimanche")
print(f"L'indice de dimanche dans jour_2 est {dimanche_index}")

#7 
nb_samedi = jour_2.count("samedi")
print(f"Le nombre de samedi dans jour_2 est {nb_samedi}")

#8 
semaine = jour_1 + jour_2
print (f"Le tuple sera finalement {semaine}")

#Exercice 2
#1

def milieu(Xa,Ya, Xb, Yb):

    return (Xa + Xb)/2 , (Ya + Yb)/2 
print(type(milieu(1,3,-1,2)))
print(milieu(1,3,-1,2))
print(f"l'abscisse du milieu est {milieu(1,3,-1,2)[0]} et l'ordonne est {milieu(1,3,-1,2)[1]}")

#4
list = []
for i in range(0, 5):
    x = str(input(f"(Nombre entré : {i}) // Entrez un nombre entier : "))
    list.append(x)
list.append(888)
list.delete(3)  
print(list)

#5
n = 20
liste = []
for i in range(n):
    nombre = randint(0, 100)
    liste.append(nombre)
print("Nombres dans la liste :")
for element in liste:
    print(element)
if len(liste) > 0:
    moyenne = sum(liste) / len(liste)
    print("La moyenne des nombres dans la liste est :", moyenne)
else:
    print("La liste est vide, impossible de calculer la moyenne.")


#6 
L1 = []
n = 6
for i in range(n):
    nombre = randint(0, 100)
    L1.append(nombre)
L2 = []
for e in range(-6, 25, 3):
    L2.append(e)
print(L2)

L3 = []
for i in range(-3, 18, 2): 
    o = i**3
    L3.append(o)
print (L3)
def echange(L, i, j):
    if 0 <= i < len(L) and 0 <= j < len(L):
        L[i], L[j] = L[j], L[i]

liste = []
for _ in range(5):
    nombre = int(input("Saisissez un nombre : "))
    liste.append(nombre)
print(f"Liste initiale : {liste}")
i = int(input("Indice de l'élément à échanger (premier indice) : "))
j = int(input("Indice de l'élément à échanger (deuxième indice) : "))
echange(liste, i, j)
print(f"Liste après l'échange : {liste}")
ListeTriee = sorted(liste)
print(f"Liste dans l'ordre : {ListeTriee}")


#7

from random import randint



def max(liste):
    max_val = liste[0]
    indice = 0
    for i in range(1, len(liste)):
        if liste[i] > max_val:
            max_val = liste[i]
            indice = i
    return max_val, indice

def min(liste):
    min_val = liste[0]
    indice = 0
    for i in range(1, len(liste)):
        if liste[i] < min_val:
            min_val = liste[i]
            indice = i
    return min_val, indice

liste20 = []
liste50 = []
for _ in range(50):
    nombre = randint(0, 100)
    liste50.append(nombre)
for _ in range(20):
    nombre = randint(0, 100)
    liste20.append(nombre)

print(f"Liste initiale : {liste20}")

max_val, indice_max = max(liste20)
print(f"Le maximum de la liste est {max_val} et son indice est {indice_max}")

print(f"Liste initiale : {liste50}")

min_val, indice_min = min(liste50)
print(f"Le minimum de la liste est {min_val} et son indice est {indice_min}")

#8
def pairs_impairs(liste): #-> on entre la liste ainsi : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    pairs = []
    impairs = []
    for i in range(len(liste)):
        if liste[i] % 2 == 0:
            pairs.append(liste[i])
        else:
            impairs.append(liste[i])
    return pairs, impairs
#9
def afficher_mode(liste):
    compteurs = {}
    for element in liste:
        if element in compteurs:
            compteurs[element] += 1
        else:
            compteurs[element] = 1

    mode = None
    max_repetitions = 0
    for element, repetitions in compteurs.items():
        if repetitions > max_repetitions:
            mode = element
            max_repetitions = repetitions

    print("Le mode de la liste est :", mode)


#10 
liste = []
for i in range(10): 
    nombre = int(input(f"Entrez le nombre {i+1} : "))
    liste.append(nombre)
    
liste_sans_doublon = list(set(liste))
print("La liste sans doublon est :", liste_sans_doublon)


#11
Mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
Annee1 = [15, 18, 19, 28, 34, 36, 45, 55, 36, 29, 17, 13]
Annee2 = [20, 21, 24, 22, 28, 34, 38, 44, 41, 31, 29, 18]
Annee3 = [17, 18, 21, 24, 32, 35, 64, 52, 47, 32, 27, 18]
tableau = [Mois, Annee1, Annee2, Annee3]

tableau = [
    ['Annee', 'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
    ['Annee1', 15, 18, 19, 28, 34, 36, 45, 55, 36, 29, 17, 13],
    ['Annee2', 20, 21, 24, 22, 28, 34, 38, 44, 41, 31, 29, 18],
    ['Annee3', 17, 18, 21, 24, 32, 35, 64, 52, 47, 32, 27, 18]
]


mois_octobre_index = tableau[0].index('Octobre')
pluie_octobre_annee2 = tableau[2][mois_octobre_index]
print(f"Nombre de mm de pluie en octobre de l'année 2 : {pluie_octobre_annee2} mm")



mois = tableau[0]
m=0
pluie_annee3 = tableau[3][1:] 
n = int(input("Entrez la hauteur de pluie a chercher: "))
for element in  pluie_annee3:
    if element == n:
        m +=1
print (f"Dans l'année 3 , il y a eu {m} fois {n} mm de pluie")




def compte_mois_h(tableau, h):
    mois = tableau[0] 
    annee1 = tableau[1]  
    annee2 = tableau[2] 
    annee3 = tableau[3] 
    nb_mois_h = 0  
    for i in range(1, len(mois)):  
        if annee1[i] == h or annee2[i] == h or annee3[i] == h:
            nb_mois_h += 1
    return nb_mois_h

hauteur_seuil = 24 # A RENTRER EN MM
nombre_de_mois = compte_mois_h(tableau, hauteur_seuil)
print(f"Nombre de mois avec une hauteur de pluie d'au moins {hauteur_seuil} mm sur trois années : {nombre_de_mois} mois.")



mois = tableau[0] 
annee1 = tableau[1]  
annee2 = tableau[2] 
annee3 = tableau[3] 

n = str(input("Voulez-vous afficher tous les mois avec une hauteur de pluie d'au moins 24 mm sur les trois années ? [Y/N] "))
if n== "Y" :
    print(f"Les mois ou il est tombé {hauteur_seuil} mm sont : ")
    for i in range(1, len(mois)):
        if annee1[i] == hauteur_seuil or annee2[i] == hauteur_seuil or annee3[i] == hauteur_seuil:
            print(mois[i])
elif n== "N" : 
    print("END")
else :
    print("ERROR")

