woerterbuch = {"tag":"day"}

while True:
    deutsch = input("Bitte deutsches Wort eingeben: ").lower()

    if deutsch == "0":
        break

    if deutsch in woerterbuch:
        print(f"Englische Übersetzung: ",{woerterbuch[deutsch]})
    else:
        print("Übersetzung nicht bekannt")
        englisch = input("Bitte englische Übersetzung eingeben: ").lower()
        woerterbuch[deutsch] = englisch