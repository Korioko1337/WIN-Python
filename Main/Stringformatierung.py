name = "Name"
stunde = 12
minute = 30

#f strings
print("Hallo Name, es ist 12:30 Uhr")
print("Hallo ", name, ", es ist ", stunde, ":", minute, " Uhr")
print("Hallo", name, ", es ist", stunde, ":", minute, "Uhr", sep="")
print(f"Hallo {name}, es ist {stunde}:{minute} Uhr")

#format funktion
print("Hallo {}, es ist {}:{}. Uhr".format(name, stunde, minute))
print("Hallo {0}, es ist {1}:{2} Uhr".format(name, stunde, minute))
print("Hallo {n}, es ist {s}:{m} Uhr".format(n=name, s=stunde, m=minute))

#formatierung ähnlich wie in C
print("Hallo %s, es ist %d:%d Uhr" % (name, stunde, minute))
