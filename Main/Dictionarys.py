woerterbuch = {"Tag":"day"}


while True:
    deutsch = input("Bitte deutsches Wort eingeben, Ende mit 0: ").lower() #umwandlung in kleinbuchstaben

    if deutsch == "0":
        break

    if deutsch in woerterbuch:
        print(f"Die Übersetzung ist:", {woerterbuch[deutsch]})
    else:
        print("Übersetzung nucht bekannt.")
        englisch = input("Bitte englische übersetzung eingeben: ")
        woerterbuch[deutsch] = englisch
        print("Wort wurde dem Wörterbuch hinzugefügt.")



woerterbuch.get(deutsch)

