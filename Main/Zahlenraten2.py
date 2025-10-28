import random

#Begrüßung
print("Zahlenraten")

#Wertebrereich festlegen
minzahl = 1
maxzahl = 100

#zu ratende Zahl festlegen
ratezahl = random.randint(minzahl, maxzahl)

zahl = None

while zahl != ratezahl:
    zahl = int(input(f"Geben Sie eine Zahl zwischen {minzahl} und {maxzahl} ein: "))

    if zahl == ratezahl:
        print("Richtig geraten!")
    elif ratezahl < zahl:
        print("Die zu ratende Zahl ist kleiner!")
    else:
        print("Die zu ratende Zahl ist größer!")
print("Spiel beendet")