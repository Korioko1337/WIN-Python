g = int(input("Geben Sie den Wert für g ein: "))
h = int(input("Geben Sie den Wert für h ein: "))
mittelwert = (g + h) / 2
if mittelwert > 50:
    print(f"Der Mittelwert von {g} und {h} ist {mittelwert} und größer als 50")
elif mittelwert == 50:
    print(f"Der Mittelwert von {g} und {h} ist {mittelwert} und  gleich 50") 
else:
    print(f"Der Mittelwert von {g} und {h} ist {mittelwert} und kleiner als 50")