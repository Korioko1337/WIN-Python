#definition der Funktion
def meine_funktion():
    print("Das ist meine Funktion!")
    print("Hier stehen Befehle innerhalb der Funktion.")

#aufruf der Funktion
meine_funktion()
meine_funktion()

"""
schlechter Programierstil, einschränkung durch feste Variable bezeichnung
"""
def berechnen1():
    #c lokale variable, nur innerhalb der Funktion
    c = a+b
    print("Die Summe der beiden Zahlen ist:", c )

a = 3
b = 5
c = 0
berechnen1()
print(c)


def berechnen2():
    zahl1 = int(input("Gib die erste Zahl ein: "))
    zahl2 = int(input("Gib die zweite Zahl ein: "))

    summe = zahl1 + zahl2
    print("Die Summe der beiden Zahlen ist:", summe)

berechnen2()

#definition der Funktion mit Parametern, platzhalter
def summe(a,b):
    ergebnis = a + b
    #print("Die Summe der beiden Zahlen ist:", ergebnis)
    #die ausgabe wird dem Programm überlassen
    return ergebnis

#aufruf der Funktion mit Argumenten
summe(4,7)

f = 4
d = 9
c = 2
summe(f,d)
print("Die Summe der beiden Zahlen ist:", summe(f,d))

s = summe(10,15)
print("Die Summe der beiden Zahlen ist:", s)

s1 = summe(f,d) + summe(c,s)

s2 = summe( summe(f,d) , summe(c,s))

print(s1)
print(s2)