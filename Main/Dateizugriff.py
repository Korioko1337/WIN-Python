"""
Dateien öffnen und schließen, schreiben und lesen
standartmodus r- lesender Zugriff
schreibmodus w- schreibender Zugriff
"""

#Datei schreiben
datei = open("test.txt", "w")

datei.write("Das ist mein Text für meine Datei\n")
datei.write("Noch mehr Text")

datei.close()

#Datei lesen
datei = open("test.txt", "r")

#dateiinhalt = datei.read()       #liest den gesamten Inhalt der Datei als einen String

dateiinhalt = datei.readlines()  #liest jede Zeile als Element in eine Liste

datei.close()

print(dateiinhalt)