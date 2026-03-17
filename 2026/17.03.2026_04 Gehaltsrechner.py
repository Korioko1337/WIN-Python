"""
Einführung in die Programmierung
Beispiel Gehaltsrechner
"""

# Anzahl Arbeitsstunden ausgeben
arbeitsstunden = 40
print("Arbeitsstunden:", arbeitsstunden)
# Stundenlohn ausgeben
stundenlohn = 20
print("Stundenlohn:", stundenlohn)

# Verdienst berechnen und ausgeben
verdienst = arbeitsstunden * stundenlohn
print("Der Verdienst beträgt:", verdienst, "Euro")
print("Verdienst:" + str(verdienst) + " Euro")
print("Verdienst: {verdienst} Euro".format(verdienst=verdienst))
print("Verdienst: {} Euro".format(verdienst))
