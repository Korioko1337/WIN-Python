# Mehrfaches Ausgeben eines Namens auf verschiedene Arten
#ausgabe des Namens 3 mal hintereinander
print("Annamaria Reinicke")
print("Annamaria Reinicke")
print("Annamaria Reinicke")

#eine zeile, 3 mal hintereinander
print("Annamaria Reinicke,", "Annamaria Reinicke,", "Annamaria Reinicke")

#string multiplikation
f = "Annamaria Reinicke "
print(f*3)

#for schleife
for i in range(3):
    print("Annamaria Reinicke")

#while schleife    
a = 0
while a < 3:
    a += 1
    print("Annamaria Reinicke")

#user input und dann 3 mal ausgeben   
name = input("Gib deinen Namen ein:") #user input
print(name*3)
    
    
    
