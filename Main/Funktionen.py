"""
Wiederholung Funktionsaufruf und eingebaute Funktionen
Beispiel Zufallszahlen
"""
#importiert Module
import random

#Ganzzahl zwischen 1 und 100 wird generiert
ganze_zahl = random.randint(1, 100)
print(f"Zufallszahl (Ganzzahl): {ganze_zahl}")

#zufällige fliesskommazahl zwischen 0 und 10 wird generiert

fliesskommazahl = random.uniform(0, 10)
#fließkommazahl wird auf 4 Nachkommastellen gerundet, round(variable, anzahlNachkommastellen)
fliesskommazahl = round(fliesskommazahl, 4)
print(f"Zufallszahl (Fliesskommazahl): {fliesskommazahl}")

