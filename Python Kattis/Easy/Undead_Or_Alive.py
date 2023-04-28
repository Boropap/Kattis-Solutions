'''
Input
The input will consist of a single line of text, no longer than 
 characters, containing letters, numbers, spaces, and any of the following symbols: .,'!?:)(.

Output
If the line contains only smiley faces and no frowny faces, then output alive.
If the line contains only frowny faces and no smiley faces, then output undead.
If the line contains both smiley faces and frowny faces, then output double agent.
Otherwise, output machine.
'''

x  = input()

if (":)" in x) == True and (":(" in x) == True:
    print("Double Agent")

elif (":)" in x) == True:
    print("Alive")

elif (":(" in x) == True:
    print("Undead")

else:
    print("Machine")
