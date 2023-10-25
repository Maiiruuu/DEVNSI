#-*-coding:utf-8 -*-
#Begue Gabriel
#TD1 - Exercice 6

age = int(input("Entrez votre age"))
    
if age < 13 :
    print ("Cela sera gratuit")
elif age > 13 and age < 25 :
    print ("vous bénificiez d'un tarif jeune de 40%")
elif age > 26 and age < 59 :
    print ("Vous payez plein pots")
elif age > 60 :
    print ("vous bénificiez d'un tarif Sénior de -20%")
elif age < 0  :
    print ("Vous n'etes pas né")
    

