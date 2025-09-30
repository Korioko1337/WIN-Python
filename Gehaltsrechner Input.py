#Gehaltsrechner mit user input
#definition der Variabeln stundenlohn und arbeitsstunden mit nutzerinput
stundenlohn = int(input("Gib deinen Stundenlohn ein: ",))       #festlegung des Wertes für die Variable als integer durch int()
arbeitsstunden = int(input("Gib deine Arbeitsstunden an: ",))    

#ausrechnen verdienst 
verdienst = stundenlohn*arbeitsstunden 

#ausgabe der werte
print("Arbeitsstunden: " , arbeitsstunden)
print("Stundenlohn: " , stundenlohn)
print("Verdienst: " , verdienst)