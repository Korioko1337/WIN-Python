for i in 1,2,3,4,5:
    print(i)

for i in range(5):
    print("Hallo")

for i in range(1,6):
    print(i)

#die 2 gibt an, dass immer 2 Zahlen übersprungen werden
#startwert, stopwert, schrittweite
for i in range(1,6,2):
    print(i)

#bis 100 zählen
for i in range(1,101):
    print(f"{i} Hallo")

#von 100 bis 1 zählen
for i in range(1,101):
    print(f"{101-i} Hallo")


for i in range(100,0,-1):
    print(f"{i} Hallo")


#in 2er schritten bis 100 zählen
for i in range(101,2):
    print(f"{i} Hallo")