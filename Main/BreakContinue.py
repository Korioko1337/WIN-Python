print("for-Schleifen mit continue:")
for i in range(-10,10):
    if i==0:
        #continue überspringt den aktuellen Schleifendurchlauf
        continue
    print(i)

print("while-Schleifen mit break:")
for i in range(-10,11):
    if i==0:
        #break beendet die Schleife komplett
        break
    print(i)

