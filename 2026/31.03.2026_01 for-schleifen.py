"""
Einführung in die Programmierung
for-Schleifen
"""

print("for-Schleife:")

for i in 1,2,3,4,5:
    print("Hallo Welt")

print("--")

for i in "1", "b", "c", "d", 3, 4, 6:
    print("Hallo Welt")

"""
Die range()-Funktion kann in drei Varianten verwendet werden:
  range(stop) – alle Zahlen von 0 bis stop-1 mit Schrittweite 1
  range(start, stop) – alle Zahlen von start bis stop-1 mit Schrittweite 1
  range(start, stop, step) – alle Zahlen von start bis stop-1 mit Schrittweite step
"""

print("for-Schleife mit range():")

for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)