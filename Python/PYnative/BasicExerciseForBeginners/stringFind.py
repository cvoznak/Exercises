#Exercise 7: Return the count of a given substring from a string

text = input("Type desired text to be checked: ")
word = input("Which word do you wish count?")

wordRepetion = text.count(word)

print(f"{word} appeared {wordRepetion} times")