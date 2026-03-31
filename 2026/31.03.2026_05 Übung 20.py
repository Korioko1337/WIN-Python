"""
Einführung in die Programmierung
Übung 20: Quadratzahlen berechnen (Skript Seite 81)

Ein Programm soll die Quadrate der Zahlen von 1 bis 100 berechnen und ausgeben.

Realisieren Sie die Berechnung zunächst mit einer for- und dann mit einer while-Schleife.
"""

#for-schleife
for i in range(1,101,1):
    print (i, i*i)

#while-schleife
i = 1

while i <= 100:
    print (i, i*i)
    i += 1