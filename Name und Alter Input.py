#definition der Variabeln name und age mit nutzerinput, text in der klammer wird bei abfrage angezeigt
name = input("Gib deinen Namen ein: ")  
age = int(input("Gib dein Alter an: ")) #Alter als Integer, deshalb int()

#Berechnung des Alters in Tagen
ageDays = age*365

#Ausgabe des Namens mit Begrüßung und des Alters in Tagen
print("Hallo", name, ", du bist", ageDays, "Tage alt.")