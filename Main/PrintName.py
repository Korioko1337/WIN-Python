# Mehrfaches Ausgeben eines Namens auf verschiedene Arten
#ausgabe des Namens 3 mal hintereinander
print("Vorname Nachname")
print("Vorname Nachname")
print("Vorname Nachname")

#eine zeile, 3 mal hintereinander
print("Vorname Nachname,", "Vorname Nachname,", "Vorname Nachname")

#string multiplikation
f = "Vorname Nachname "
print(f*3)

#for schleife
for i in range(3):
    print("Vorname Nachname")

#while schleife    
a = 0
while a < 3:
    a += 1
    print("Vorname Nachname")

#user input und dann 3 mal ausgeben   
name = input("Gib deinen Namen ein:") #user input
print(name*3)
    
    
    
