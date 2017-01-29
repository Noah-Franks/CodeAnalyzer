import os
import shutil

filePath = input("Please provide a file to analyze\n")

print(filePath)


letterSpace  = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
letterSpace += "0123456789"
letterSpace += "!@#$%^&*()[]{}/?=+\|-_;:'\",.<>`~\n"
letters = []
for letter in letterSpace :
    pair = []
    pair.append(letter)
    pair.append(0)
    letters.append(pair)



with open(filePath) as fileobj:
    for word in fileobj:  
       for ch in word: # A character by character read of the file

           chMatchFound = False
           for l in range(len(letterSpace)) :
               if letterSpace[l] == ch :
                   letters[l][1] += 1
                   chMatchFound = True
                   break
           if not chMatchFound :
               print("Unmatched Letter Found " + ch)
            
consoleWidth = shutil.get_terminal_size().columns - 12

for letter in letters :
    if letter[1] is not 0 :
        bar = ""
        if letter[1] < consoleWidth :
            for i in range(letter[1]) :
                bar += "#"
        else :
            for i in range(consoleWidth) :
                bar += "#"
        print(repr(letter[0]) + " " + bar + " " + str(letter[1]))
        

