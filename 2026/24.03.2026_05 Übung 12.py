"""
Einführung in die Programmierung
Übung 12: Bereich einer Zahl prüfen (Skript Seite 79)

Schreiben Sie ein Programm, das überprüft, ob eine vom Benutzer eingegebene
Ganzzahl im Bereich von 0 bis einschließlich 100, 101 bis einschließlich 200
oder außerhalb dieser beiden Bereiche liegt und dies entsprechend ausgibt.
"""

zahl = int(input("Bitte Zahl eingeben"))

if 0 < zahl <100:
    print("Die Zahl liegt zwischen 0 und 100.")
elif 101 <= zahl <=200:
    print("Die Zahl liegt zwischen 101 und 200.")
else:
    print("Die Zahl liegt außerhalb des Bereichs.")