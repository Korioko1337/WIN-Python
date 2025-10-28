"""
i/j  0  1  2  3  4  5  6  7 
                                anzahl - 1                     
0    1  0  0  0  0  0  0  1     0 7 
1    0  1  0  0  0  0  1  0     1 6
2    0  0  1  0  0  1  0  0     2 5
3    0  0  0  1  1  0  0  0     3 4
4    0  0  0  1  1  0  0  0     4 3
5    0  0  1  0  0  1  0  0     5 2
6    0  1  0  0  0  0  1  0     6 1
7    1  0  0  0  0  0  0  1     7 0
"""

n = int(input("Größe der Matrix: "))
for i in range(n):
    for j in range(n):
        print("1  " if (i == j or i + j == n - 1) else "0  ", end="")
    print()


anzahl = int(input("Größe der Matrix: "))
for i in range(anzahl):
    for j in range(anzahl):
        if i==j or i+j==anzahl-1:
            #end=" " sorgt dafür, dass kein Zeilenumbruch erfolgt, somit wird j für jedes i in
            #einer Zeile ausgegeben
            print("1 ", end=" ")
        else:
            print("0 ", end=" ")
    #Zeilenumbruch nach jeder i-Schleife
    print()