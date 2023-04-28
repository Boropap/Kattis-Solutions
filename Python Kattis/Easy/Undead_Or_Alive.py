x  = input()

if (":)" in x) == True and (":(" in x) == True:
    print("Double Agent")

elif (":)" in x) == True:
    print("Alive")

elif (":(" in x) == True:
    print("Undead")

else:
    print("Machine")