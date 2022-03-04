#Exercise 6: Display numbers divisible by 5 from a list

#create a empty list
originList = []

n = None #create an empty variable
countElement = 0 #create a variable to count list elements

while n != 0: #loop until n different zero 0, there is a limitation to append (add) zero to list
    n = int(input("type list element, or 0 to end list: "))
    if n != 0:#if different of zero append as a new item in list
        originList.append(n)
        countElement += 1

print(f"Given list is: {originList}") #show input list

divNumber = float(input("Do you wish list divisible by? ")) #Request to user to input a value to be used in division

print(f"Divisible by {divNumber}:")

for i in range(0, countElement):#loop with "for" with a limitation of repetion using "countElement"
    finalNumber = originList[i] / divNumber
    print(finalNumber)


