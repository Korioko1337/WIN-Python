n = int(input("Größe derMatrix: "))
for i in range(n):
    for j in range(n):
        print("1  " if (i == j or i + j == n - 1) else "0  ", end="")
    print()


anzahl = int(input("Größe derMatrix: "))
for i in range(anzahl):
    for i in range(anzahl):
        print("0  ", end=" ")
    print()
