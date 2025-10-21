#zahlendreieck
"""alternative Lösung
for i in range(1,9):
    f = str(i)
    print(f*i)
"""

for i in range(1,9):
    print(f"{i} "*i)
    #print(str(i)*i)


#zentriertes zahlendreieck
for i in range(1,9):
    print(" "*(8-i)+f"{i} "*i)

