"""
Einführung in die Programmierung
Übung 1: Namen auf dem Bildschirm ausgeben (Skript Seite 77)

Schreiben Sie ein Programm, das Ihren Namen dreimal auf dem Bildschirm ausgibt.

Ergänzen Sie das Programm um sinnvolle Kommentare.
"""

print("Annamaria Reinicke")
print("Annamaria Reinicke")
print("Annamaria Reinicke")

print("Annamaria Reinicke", "Annamaria Reinicke", "Annamaria Reinicke")

print("Annamaria Reinicke Annamaria Reinicke Annamaria Reinicke")

print("Annamaria Reinicke"); print("Annamaria Reinicke"); print("Annamaria Reinicke")

print("Annamaria Reinicke\n"*3) #\n sorgt für einen Zeilenumbruch

#variable definieren, initialisierung
n = "Annamaria Reinicke "

#dreimal ausgeben
print(n*3)

#dreimal ausgeben mit for schleife
for i in range (3):
    print(n)

#konstante variabeln in uppercase