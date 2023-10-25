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
