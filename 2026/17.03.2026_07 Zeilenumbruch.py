"""
Einführung in die Programmierung
Ausgabe
"""
test = 1234
# Ausgabe auf dem Bildschirm erfolgt über die Funktion print():
print("Hallo", 1234, "Welt", test, True)

# Trennzeichen zwischen einzelnen auszugebenden Elementen kann durch den
# benannten Parameter sep geändert werden:
print("Hallo", 1234, "Welt", test, True, sep=" - ") 
#- kann durch beliebeige Zeichenkette ersetzt werden
#sep bedeutet separator, also Trennzeichen

# Standardmäßig wird am Ende ein Zeilenumbruch (Newline) ausgegeben.
# Durch den benannten Parameter end kann dies beeinflusst werden:
print("Hallo", end=" ")# kann durch beliebige Zeichenkette ersetzt werden, kein Zeilenumbruch mehr
print("Welt")

# Zeilenumbruch in einer Print anweisung:
print("Hallo", 1234, "\n", "Welt", test, True, sep=" - ") 