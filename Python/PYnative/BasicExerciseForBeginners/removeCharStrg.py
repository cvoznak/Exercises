#Exercise 4: Remove first n characters from a string
#Write a program to remove characters from a string starting from zero up to n and return a new string.

#Entry string, independent if is word or phrase.
string = input("Type a word or a phrase: ")

#Require to user how many character wish to remove from start
n = int(input("How many characters do you wish remove? "))

#slice string - [start:end:step]
newString = string[n:]

print(newString)