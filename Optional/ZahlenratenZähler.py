#modul random wird importiert
import random

print("Willkommen")

#Eingabe der Zahl, die geraten wird
t = int(input("Erraten Sie die Zahl zwischen 1 und 10: "))

#Zufallszahl zwischen 1 und 10 wird generiert
number = random.randint(1,10)     

a=0
while a != 3 and t != number: 
        if t < number:
            t = int(input("Falsch geraten, die gesuchte Zahl ist größer, versuchen Sie es erneut: "))  
        else:
           t = int(input("Falsch geraten, die gesuchte Zahl ist kleiner, versuchen Sie es erneut: "))
        a = a + 1

if t == number:
    print("Richtig :)")
else:
    print(f"Verloren :(, die zahl war {number}")
