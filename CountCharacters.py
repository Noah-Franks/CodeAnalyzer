import os

filePath = input()

print(filePath)


letterSpace = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = []
for letter in letterSpace :
    pair = []
    pair.append(letter)
    pair.append(0)
    letters.append(pair)

for letter in letters :
    print(letter)

'''
with open(filePath) as fileobj:
    for word in fileobj:  
       for ch in word: 
           print (ch);'''
