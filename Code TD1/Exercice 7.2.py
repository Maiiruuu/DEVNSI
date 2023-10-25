
#-*-coding:utf-8 -*-
#Begue Gabriel
#TD1 - Exercice 7.2

n = float(input("Combien de nombres souhaitez-vous ?  "))
if n is float :
    print('ereur')
Total = 0
for i in range (n):
    if n%2 != 1 :
        Total=Total +2*n
print(Total)