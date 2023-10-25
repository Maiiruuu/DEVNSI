import tkinter as tk
import pyperclip  


def copier():
    result_text = resultat.get()
    pyperclip.copy(result_text)
def binairedecimal(ficelle):
    x = len(ficelle) - 1
    n = 0
    res = 0
    while x != -1:
        if ficelle[x] == "1":
            res = res + 2 ** n
        n = n + 1
        x = x - 1
    return res

def decimalbinaire(ficelle):
    quotient = int(ficelle)
    res = ""
    while quotient != 1:
        res = res + str(quotient % 2)
        quotient = quotient // 2
    res = res + "1"
    return res

def binairehexa(ficelle):
    res = ""
    while len(ficelle) > 4:
        res = ficelle[-4:] + res  
        ficelle = ficelle[:-4]
    res = ficelle + res  
    while len(res) % 4 != 0:
        res = "0" + res 
    return res

def hexabinaire(ficelle):
    res = ""
    for x in range(len(ficelle)):
        res = res + format(int(ficelle[x], 16), '04b')
    return res

def decimalhexa(ficelle):
    return binairehexa(decimalbinaire(ficelle))

def hexadecimal(ficelle):
    return str(hex(int(ficelle)))

def decimaloctal(ficelle):
    return oct(int(ficelle))

def octal(ficelle):
    return str(oct(int(ficelle)))

def converter():
    saisie = Esaisie.get()
    x, y = basedepart.get(), basearrivee.get()
    couple = (x, y)
    if couple == (1, 2):
        res = decimalbinaire(saisie)
    elif couple == (1, 3):
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
'''
def add_bin(binaire1, binaire2): #defectueux 
    if len(binaire1) != 8 or len(binaire2) != 8:
        return "Les deux nombres doivent être de 8 bitss."

    num1 = int(binaire1, 2)
    num2 = int(binaire2, 2)

    somme = num1 + num2

    if somme < 0:
        somme = 0
    elif somme > 255:
        somme = 255

    resultat = format(somme, '08b')

    return resultat
'''
def inverse_binaire(binaire):
    if len(binaire) != 8:
        raise ValueError("La chaîne binaire doit contenir exactement 8 bitss.")
    
    inverse = ""
    for bits in binaire:
        if bits == '0':
            inverse += '1'
        elif bits == '1':
            inverse += '0'
        else:
            raise ValueError("La chaîne binaire ne doit contenir que des 0 et des 1.")
    
    return inverse
    
########################################################################################
def afficher_convertisseur_multibases():
    root.title("Convertisseur Multi-bases par Gabriel")
    bouton_operation_binaire.config(state=tk.DISABLED)

def converter():
    saisie = Esaisie.get()
    x, y = basedepart.get(), basearrivee.get()
    couple = (x, y)
    conversions = {
        (1, 2): decimalbinaire,
        (1, 3): decimalhexa,
        (1, 4): decimaloctal,
        (2, 1): binairedecimal,
        (2, 3): binairehexa,
        (2, 4): lambda x: octal(decimalbinaire(x)),
        (3, 1): hexadecimal,
        (3, 2): hexabinaire,
        (3, 4): lambda x: octal(int(x, 16)),
        (4, 1): octal,
        (4, 2): lambda x: octal(binairedecimal(x)),
        (4, 3): lambda x: octal(int(x, 16)),
    }
    res = conversions.get(couple, lambda x: "Erreur 404")(saisie)
    resultat.set(res)

def create_conversion_ui():
    tk.Label(root, text="Saisissez la valeur à convertir").pack(side=tk.TOP)
    global Esaisie
    Esaisie = tk.Entry(root)
    Esaisie.pack(side=tk.TOP)

    Fgauche = tk.Frame(root)
    Fgauche.pack(side=tk.LEFT)
    tk.Label(Fgauche, text="Base de départ").pack()
    global basedepart
    basedepart = tk.IntVar()
    base_labels = ["Decimal", "Binaire", "Hexadecimal", "Octal"]
    for i, label in enumerate(base_labels, start=1):
        tk.Radiobutton(Fgauche, text=label, variable=basedepart, value=i, indicatoron=0, width=20).pack()

    Fdroite = tk.Frame(root)
    Fdroite.pack(side=tk.RIGHT)
    tk.Label(Fdroite, text="Base d'arrivée").pack()
    global basearrivee
    basearrivee = tk.IntVar()
    for i, label in enumerate(base_labels, start=1):
        tk.Radiobutton(Fdroite, text=label, variable=basearrivee, value=i, indicatoron=0, width=20).pack()

    global resultat
    Bconvertir = tk.Button(root, text="Convertir", command=converter)
    Bconvertir.pack(side=tk.BOTTOM)

    resultat = tk.ficelleVar()
    result_label = tk.Label(root, textvariable=resultat)
    result_label.pack(side=tk.BOTTOM)

def menu_operation_binaire():
    fenetre_operation = tk.Toplevel(root)
    fenetre_operation.title("Addition et Soustraction Binaires")

    tk.Label(fenetre_operation, text="Saisir le premier nombre binaire :").pack()
    binaire_num1 = tk.Entry(fenetre_operation)
    binaire_num1.pack()

    tk.Label(fenetre_operation, text="Saisir le deuxième nombre binaire :").pack()
    binaire_num2 = tk.Entry(fenetre_operation)
    binaire_num2.pack()

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

    resultat = operation(int(binaire_num1.get(), 2), int(binaire_num2.get(), 2))
    etiquette_resultat.config(text=f"Résultat binaire: {(resultat)[2:]}")

def inverse_binaire(binaire):
    if len(binaire) != 8:
        raise ValueError("La chaîne binaire doit contenir exactement 8 bitss.")
    
    inverse = ""
    for bits in binaire:
        if bits == '0':
            inverse += '1'
        elif bits == '1':
            inverse += '0'
        else:
            raise ValueError("La chaîne binaire ne doit contenir que des 0 et des 1.")
    
    return inverse

def menu_inverse_binaire():
    fenetre_operation = tk.Toplevel(root)
    fenetre_operation.title("Inverse Binaires")

    tk.Label(fenetre_operation, text="Saisir le premier nombre binaire :").pack()
    binaire_num1 = tk.Entry(fenetre_operation)
    binaire_num1.pack()
    tk.Button

root = tk.Tk()
root.title("Convertisseur Mulit-bases et Addition / Soustraction Binaires par Maiiruuu")

create_conversion_ui()

Bcopier = tk.Button(root, textvariable=resultat, command=copier)
Bcopier.pack(side=tk.BOTTOM)

tk.Button(root, text="Addition/Soustraction Binaires",command=menu_operation_binaire).pack()
tk.Button(root, text="Inverse du nombre binaire", command=menu_inverse_binaire()).pack()
bouton_operation_binaire = tk.Button(root, text="Ouvrir le menu", command=menu_operation_binaire, state=tk.DISABLED)
bouton_operation_binaire.pack(side=tk.BOTTOM)

root.mainloop()
