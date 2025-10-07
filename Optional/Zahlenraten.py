#modul random wird importiert
import random

print("Willkommen")

#Eingabe der Zahl, die geraten wird
t = int(input("Erraten Sie die Zahl zwischen 1 und 10: "))

#Zufallszahl zwischen 1 und 10 wird generiert 
number = random.randint(1,10)


#wenn die Zahl richtig geraten wurde, wird gewonnen, ansonsten verloren
if t == number:
    print("Gewonnen :)")
else:
    print("Verloren, die gesuchte Zahl war", number ,  ":(")


print("Das Spiel ist beendet.")