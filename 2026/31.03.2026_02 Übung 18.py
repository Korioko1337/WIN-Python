"""
Einführung in die Programmierung
Übung 18: Wiederholte Ausgabe (Skript Seite 80)

Schreiben Sie ein Programm, dass 100mal hintereinander das Wort "Hallo" ausgibt.
Nutzen Sie dazu die for-Schleife.

Ergänzung 1: Vor dem Wort "Hallo" soll jeweils der aktuelle Zählerstand ausgeben
             werden.

Ergänzung 2: Es soll die gleiche Ausgabe wie in Ergänzung 1 erfolgen, jedoch
             soll rückwärts gezählt werden.

Ergänzung 3: Es soll wieder vorwärts gezählt werden, aber diesmal in
             2er-Schritten von 2 bis 100.
"""

for i in range(1,101):
    print(i, "Hallo")

for i in range(100,0,-1):
    print(f"{i} Hallo")

for i in range(2,101,2):
    print(i, "Hallo")