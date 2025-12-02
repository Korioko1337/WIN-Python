"""
Syntaxfehler
Laufzeitfehler
Logischerfehler
"""
"""
# Syntaxfehler

def summe(a,b):
    c = a + b
    return c

#bsp klammer zu wenig
#for i in range(int(input("Bitte eine Zahl eingeben: ")):
for i in range(int(input("Bitte eine Zahl eingeben: "))):
    erg = summe(i, i*i)
    print(erg)
"""
# Logischerfehler
"""
def printlist(printlist):

    liste =[printlist]
    for i in range(len(liste)):
        print(i)

data = [1,2,3,4,5]
printlist(data)

def printlist(printlist):

    liste = printlist
    for i in range(len(liste)):
        print(i)

data = [1,2,3,4,5]
printlist(data)
"""

#try except Blöcke

x = input("Bitte eine Zahl x eingeben: ")
y = input("Bitte eine Zahl y eingeben: ")

try:
    erg = int(x) / int(y)

# Keine Zahl eingegeben
except ValueError:
    print("Fehrler: Keine Zahl!")

# Division durch Null
except ZeroDivisionError:
    print("Fehler: Division durch Null nicht möglich!")

# Alle anderen Fehlermeldungen
except:
    print("Allgemeiner Fehler!")
else:
    print("Ergebnis: ", erg)
finally:
    print("Ende des Programms.")
