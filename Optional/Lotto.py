import random

print("Willkommen")

tipp = int(input("Gib deine Lotto Zahlen zwischen 1 und 49 ein: "))         #Eingabe der Zahlen, die geraten wird

lotto_zahl = list(range(1, 50))
number = random.sample(lotto_zahl, 6)                                      #6 Zufallszahlen zwischen 1 und 49 werden generiert
number.sort()

if tipp == number:
    print("Gewonnen :)")
else:
    print(f"Verloren, die Lotto Zahlen waren {number} :(")