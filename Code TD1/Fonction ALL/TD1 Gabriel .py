# TD1 - Exercice 1
def Exercice1(nombre):
    print("Programme pour vérifier si un nombre est pair ou impair")
    if nombre % 2 == 0:
        return "Pair"
    else:
        return "Impair"

# TD1 - Exercice 2
def Exercice2():
    print("Compteur de 0 à 10")
    for i in range(11):
        print(i)
    print("Décollage")

# TD1 - Exercice 3
def Exercice3():
    print("Calcul des 12 premiers multiples de 7")
    resultat = []
    for i in range(1, 13):
        n = i + 1
        resultat.append(7 * n)
    return resultat

# TD1 - Exercice 4
def Exercice4():
    print("Calcul de la moyenne de trois notes")
    print("Veuillez saisir vos notes pour calculer la moyenne")
    Pn = float(input("Première note : "))
    Dn = float(input("Deuxième note : "))
    Tn = float(input("Troisième note : "))
    moyenne = (Pn + Dn + Tn) / 3
    return moyenne

# TD1 - Exercice 5
def Exercice5(prix_htc):
    print("Calcul du prix TTC à partir du prix HT")
    prix_ttc = prix_htc + prix_htc * 0.2  # Correction du calcul de la TVA (20%)
    return prix_ttc

# TD1 - Exercice 6
def Exercice6(age):
    print("Détermination de la catégorie tarifaire en fonction de l'âge")
    if age < 0:
        return "Vous n'êtes pas encore né"
    elif age < 13:
        return "Cela sera gratuit"
    elif age < 25:
        return "Vous bénéficiez d'un tarif jeune de 40%"
    elif age < 59:
        return "Vous payez plein tarif"
    else:
        return "Vous bénéficiez d'un tarif sénior de -20%"

# TD1 - Exercice 7
def Exercice7():
    print("Calcul de la somme des premiers nombres pairs et impairs jusqu'à un nombre donné")
    def est_entier(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def somme_premiers_nombres_paires_impaires(n):
        somme_paires = 0
        somme_impaires = 0
        i = 1

        while n > 0:
            if i % 2 == 0:
                somme_paires += i
            else:
                somme_impaires += i
            i += 1
            n -= 1

        return somme_paires, somme_impaires

    while True:
        n = input("Entrez un nombre entier n : ")

        if est_entier(n):
            n = int(n)
            if n < 1:
                print("Veuillez entrer un nombre entier positif.")
            else:
                somme_paires, somme_impaires = somme_premiers_nombres_paires_impaires(n)
                print(f"La somme des {n} premiers nombres pairs est : {somme_paires}")
                print(f"La somme des {n} premiers nombres impairs est : {somme_impaires}")
                break
        else:
            print("Veuillez entrer un nombre entier valide.")

# TD1 - Exercice 8
def Exercice8():
    print("Calcul de la somme des premiers nombres pairs et impairs jusqu'à un nombre donné (version 2)")
    def est_entier(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def somme_premiers_nombres_paires_impaires(n):
        somme_paires = 0
        somme_impaires = 0
        i = 1

        while n > 0:
            if i % 2 == 0:
                somme_paires += i
            else:
                somme_impaires += i
            i += 1
            n -= 1

        return somme_paires, somme_impaires

    while True:
        n = input("Entrez un nombre entier n : ")

        if est_entier(n):
            n = int(n)
            if n < 1:
                print("Veuillez entrer un nombre entier positif.")
            else:
                somme_paires, somme_impaires = somme_premiers_nombres_paires_impaires(n)
                print(f"La somme des {n} premiers nombres pairs est : {somme_paires}")
                print(f"La somme des {n} premiers nombres impairs est : {somme_impaires}")
                break
        else:
            print("Veuillez entrer un nombre entier valide.")
while True :
    r = int(input("Entrer l'exercice a executer entre 1 et 8 :"))

    if r == 1 :
        print(Exercice1)
    if r == 2 :
        print(Exercice2)
    if r == 3 :
        print(Exercice3)
    if r == 4 :
        print(Exercice4)
    if r == 5 :
        print(Exercice5)
    if r == 6 :
        print(Exercice6)
    if r == 7 :
        print(Exercice7)
    if r == 8 :
        print(Exercice8)

