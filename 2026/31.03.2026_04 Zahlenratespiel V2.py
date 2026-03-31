"""
Einführung in die Programmierung
Zahlenratespiel V2 - Erweiterung um eine Schleife

Aufgabe: Wenn der Nutzer die Zahl nicht erraten hat, soll das Programm
wiederholt nach einer weiteren Zahl fragen
"""

# Begrüßung
print("Willkommen zum Zahlenratespiel")

# Zu ratende Zahl festlegen
zahl = 12   # wird im Laufe des Semesters durch Zufallszahl ersetzt

# Zahl eingeben und in Ganzzahl umwandeln
eingabe = int(input("Bitte geben Sie Ihre zu ratende Zahl ein: "))

# Eingegebene Zahl mit zu ratender Zahl vergleichen
if eingabe == zahl:
    print("Sie haben gewonnen, die Zahl wurde erraten!")
else:
    print("Sie haben verloren, die Zahl wurde nicht erraten!")

# Spiel beenden

