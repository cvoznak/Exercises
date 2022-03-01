#Exercise 3: Print characters from a string that are present at an even index number

#word input by user
word = input("Enter word: ")
#shows word input confirmation
print(f"Original string is {word}")

#get the length of a string
size = len(word)

#loop to print character by character, since letter 0 until last, always start count with 0 and runs until size-1
for i in range(0, size):
    print(f"index [{i + 1}] {word[i]}")