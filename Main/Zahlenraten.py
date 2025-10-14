print("Zahlenratespiel")

ratezahl = 15

zahl = ratezahl + 1
#zahl = None

while zahl != ratezahl:
    zahl = int(input("Geben Sie eine Zahl zwischen 1 und 20 ein: "))
    
    if zahl == ratezahl:
        print("Richtig geraten!")
    else:
        print("Falsch geraten")
