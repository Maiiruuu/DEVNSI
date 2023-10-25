#-*-coding:utf-8 -*-
#Begue Gabriel
from random import*
from math import* 

def FOR() : 
    #TD1 - Exercice FOR
    Nb = 0
    Nb= int(input("Veuillez saisir le nombre dont vous voulez afficher les carrés le précédant et lui meme"))
    n=0
    for i in range(1, Nb): 
            n=n+1
            f = n**2
    return f 

def IF() : 
    #TD1 - Exercice IF
    x = randint(0,1000)#Nombre a trouver 
    y = 0
    z = 0 #Init.
    while x!=y : 
        y = int(input("Entrer le nombre entier que vous pensez etre le bon : "))#Nombre qui cherche
        if type(y) is not int :
            print("Mauvais format")
            y = int(input("Entrer le nombre entier que vous pensez etre le bon : "))#Nombre qui cherche
        z = z+1 #Incr.
        if x<y :
            print("c'est moins de " , y)
        if y<x :
            print("c'est plus de" , y)
        if z == 11 :
            print("trop de tentatives le nombre était :" , x)
    print("C'était bien ", y , "Vous avez trouvé en" , z , "tentatives")

def WHILE():
#TD1 - Exercice WHILE
    print("Ce programme permet de théoriser combien de pli de papier est necessaire pour atteindre une distance donnée" ) 
    x = int(input("Quelle distance voulez vous atteindre avec ce papier en mètre : "))
    y = 0.05
    #en mm
    n=0# nb de pli
    y=y/1000  # y en mètre
    while y<x :
        y=y*2
        n=n+1
    print(y*1000)
    print("nombre de pli(s) :" , n)
    







