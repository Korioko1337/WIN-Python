#modul random wird importiert
import random

print("Willkommen")

#Eingabe der Zahl, die geraten wird
t = int(input("Erraten Sie die Zahl zwischen 1 und 10: "))

#Zufallszahl zwischen 1 und 10 wird generiert
number = random.randint(1,10)     


#wenn die Zahl richtig geraten wurde, wird gewonnen, ansonsten verloren
while t != number:
    if t < number:
        t = int(input("Falsch geraten, die gesuchte Zahl ist größer, versuchen Sie es erneut: "))  
    else:
       t = int(input("Falsch geraten, die gesuchte Zahl ist kleiner, versuchen Sie es erneut: "))

print("Richtig :)")