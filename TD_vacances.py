def virement(somme_donnee, prix_a_payer):
    prix_a_payer = prix_a_payer * 100
    somme_donnee = somme_donnee * 100
    difference = somme_donnee - prix_a_payer

    billets = [20000, 10000, 5000, 2000, 1000, 500]
    rendu = []

    for billet in billets:
        nombre = difference // billet
        if nombre > 0:
            rendu.append((billet, nombre))
            difference -= billet * nombre

    for billet, nombre in rendu:
        return(f"Rendre {nombre} de {billet / 100:.2f}€")
