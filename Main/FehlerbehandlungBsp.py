"""
Aufgabe 65
"""

liste = [["Max Müller", "Bahnhofstr. 12", "Heilbronn"],
        ["Susi Sorglos", "Hauptstr. 8", "Berlin"]]

#Liste soll als CSV-Datei mit folgendem format gespeichert werden:
#Max Müller;Bahnhofstr. 12;Heilbronn
#Susi Sorglos;Hauptstr. 8;Berlin

adresse = ["Max Müller", "Bahnhofstr. 12", "Heilbronn"]
adressstring = ""
adressstring += adresse[0] + ";"
adressstring += adresse[1] + ";"  
adressstring += adresse[2] + "\n"
print(adressstring)

for adresse in liste:
    for i in range (len(adresse)):
        adressstring += adresse[i] + ";"
    adressstring += "\n"

print(adressstring)