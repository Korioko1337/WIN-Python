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
a = int(input("Geben Sie den Wert für a ein: "))
b = int(input("Geben Sie den Wert für b ein: "))

if a < b:
    print(f"{a} ist kleiner als {b}")


#if-else-Anweisung
c = int(input("Geben Sie den Wert für c ein: "))
d = int(input("Geben Sie den Wert für d ein: "))

if c < d:
    print(f"{c} ist kleiner als {d}")
else:
    print(f"{c} ist nicht kleiner als {d}")

#if-elif-else-Anweisung
e = int(input("Geben Sie den Wert für e ein: "))
f = int(input("Geben Sie den Wert für f ein: "))

if e < f:
    print(f"{e} ist kleiner als {f}")
elif e == b:
    print(f"{e} ist gleich {f}")    
else:
    print(f"{e} ist größer als {f}")    


x = int(input("Geben Sie eine Zahl ein: "))
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