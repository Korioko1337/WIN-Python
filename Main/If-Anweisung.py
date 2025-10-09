"""
Vergleichsoperatoren und if-Anweisungen
< kleiner als
> größer als
<= kleiner gleich
>= größer gleich
== gleich
!= ungleich
"""

#if-Anweisung
a = 10
b = 20

#Wenn a kleiner als b ist, dann ...
if a < b:
    print(f"{a} ist kleiner als {b}")


#if-else-Anweisung, wenn a kleiner als b ist, dann ..., sonst ...
a = 10
b = 20

if a < b:
    print(f"{a} ist kleiner als {b}")
else:
    print(f"{a} ist nicht kleiner als {b}")

#Wenn a kleiner als b ist, dann ..., wenn a gleich b ist, dann ..., sonst ...
#if-elif-else-Anweisung
a = 10
b = 20

if a < b:
    print(f"{a} ist kleiner als {b}")
elif a == b:
    print(f"{a} ist gleich {b}")    
else:
    print(f"{a} ist größer als {b}")    


x = 15
if( x % 2) == 0:
    print(f"{x} ist gerade")
else:
    print(f"{x} ist ungerade")


g = int(input("Geben Sie den Wert für g ein: "))
h = int(input("Geben Sie den Wert für h ein: "))
mittelwert = (g + h) / 2

if mittelwert > 50:
    print(f"Der Mittelwert von {g} und {h} ist {mittelwert} und größer als 50")
elif mittelwert == 50:
    print(f"Der Mittelwert von {g} und {h} ist {mittelwert} und  gleich 50") 
else:
    print(f"Der Mittelwert von {g} und {h} ist {mittelwert} und kleiner als 50")