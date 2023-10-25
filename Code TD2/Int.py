from logging import root
import tkinter as tk
import pyperclip

def copier():
    result_text = resultat.get()
    pyperclip.copy(result_text)

def copierinverse():
    e = inv.get()
    pyperclip.copy(e)

def binairedecimal(string):
    x = len(string) - 1
    n = 0
    res = 0
    while x != -1:
        if string[x] == "1":
            res = res + 2 ** n
        n = n + 1
        x = x - 1
    return res

def decimalbinaire(string):
    quotient = int(string)
    res = ""
    while quotient != 1:
        res = res + str(quotient % 2)
        quotient = quotient // 2
    res = res + "1"
    return res

def binairehexa(string):
    res = ""
    while len(string) > 4:
        res = string[-4:] + res
        string = string[:-4]
    res = string + res
    while len(res) % 4 != 0:
        res = "0" + res
    return res

def hexabinaire(string):
    res = ""
    for x in range(len(string)):
        res = res + format(int(string[x], 16), '04b')
    return res

def decimalhexa(string):
    return binairehexa(decimalbinaire(string))

def hexadecimal(string):
    return str(hex(int(string)))

def decimaloctal(string):
    return oct(int(string))

def octal(string):
    return str(oct(int(string)))

def converter():
    saisie = saisie_valeur.get()
    x, y = base_depart.get(), base_arrivee.get()
    couple = (x, y)
    if couple == (1, 2):
        res = decimalbinaire(saisie)
        res = decimalhexa(saisie)
    elif couple == (1, 4):
        res = decimaloctal(saisie)
    elif couple == (2, 1):
        res = binairedecimal(saisie)
    elif couple == (2, 3):
        res = binairehexa(saisie)
    elif couple == (2, 4):
        res = octal(decimalbinaire(saisie))
    elif couple == (3, 1):
        res = hexadecimal(saisie)
    elif couple == (3, 2):
        res = hexabinaire(saisie)
    elif couple == (3, 4):
        res = octal(int(saisie, 16))
    elif couple == (4, 1):
        res = octal(saisie)
    elif couple == (4, 2):
        res = octal(binairedecimal(saisie))
    elif couple == (4, 3):
        res = octal(int(saisie, 16))
    else:
        res = "Erreur 404"

    resultat.set(res)

def inverse_binaire(binaire):
    if len(binaire) != 8:
        raise ValueError("La chaîne binaire doit contenir exactement 8 bits.")

    inverse = ""
    for bit in binaire:
        if bit == '0':
            inverse += '1'
        elif bit == '1':
            inverse += '0'
        else:
            raise ValueError("La chaîne binaire ne doit contenir que des 0 et des 1.")

    return inverse

def afficher_convertisseur_multibases():
    root.title("Convertisseur Multi-bases par Gabriel")
    bouton_operation_binaire.config(state=tk.DISABLED)
 
def creer_interface_conversion():
    tk.Label(root, text="Entrez la valeur à convertir").pack(side=tk.TOP)
    global saisie_valeur
    saisie_valeur = tk.Entry(root)
    saisie_valeur.pack(side=tk.TOP)

    cadre_gauche = tk.Frame(root)
    cadre_gauche.pack(side=tk.LEFT)
    tk.Label(cadre_gauche, text="Base de départ").pack()
    global base_depart
    base_depart = tk.IntVar()
    labels_bases = ["Décimal", "Binaire", "Hexadécimal", "Octal"]
    for i, label in enumerate(labels_bases, start=1):
        tk.Radiobutton(cadre_gauche, text=label, variable=base_depart, value=i, indicatoron=0, width=20).pack()

    cadre_droite = tk.Frame(root)
    cadre_droite.pack(side=tk.RIGHT)
    tk.Label(cadre_droite, text="Base d'arrivée").pack()
    global base_arrivee
    base_arrivee = tk.IntVar()
    for i, label in enumerate(labels_bases, start=1):
        tk.Radiobutton(cadre_droite, text=label, variable=base_arrivee, value=i, indicatoron=0, width=20).pack()

    global resultat
    bouton_convertir = tk.Button(root, text="Convertir", command=converter)
    bouton_convertir.pack(side=tk.BOTTOM)

    resultat = tk.StringVar()
    etiquette_resultat = tk.Label(root, textvariable=resultat)
    etiquette_resultat.pack(side=tk.BOTTOM)

def menu_operation_binaire():
    fenetre_operation = tk.Toplevel(root)
    fenetre_operation.title("Addition et Soustraction Binaires")

    tk.Label(fenetre_operation, text="Saisir le premier nombre binaire :").pack()
    binaire_num1 = tk.Entry(fenetre_operation)
    binaire_num1.pack()

    tk.Label(fenetre_operation, text="Saisir le deuxième nombre binaire :").pack()
    binaire_num2 = tk.Entry(fenetre_operation)
    binaire_num2.pack()

    etiquette_resultat = tk.Label(fenetre_operation, text="")
    etiquette_resultat.pack()

    def operation_binaire(operation):
        try:
            resultat = operation(int(binaire_num1.get(), 2), int(binaire_num2.get(), 2))
            etiquette_resultat.config(text=f"Résultat binaire: {bin(resultat)[2:]}")
        except ValueError:
            etiquette_resultat.config(text="Saisie binaire invalide")

    bouton_addition = tk.Button(fenetre_operation, text="Addition", command=lambda: operation_binaire(int.__add__))
    bouton_addition.pack()

    bouton_soustraction = tk.Button(fenetre_operation, text="Soustraction", command=lambda: operation_binaire(int.__sub__))
    bouton_soustraction.pack()

def menu_inverse_binaire():
    fenetre_operation = tk.Toplevel(root)
    fenetre_operation
