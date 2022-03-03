#Exercise 5: Check if the first and last number of a list is the same
#create a function to check first and last element
def first_last_same(numberList):
    print(f"Given list: {numberList}") #shows list to be checked

    firstNum = numberList[0]
    lastNum = numberList[-1]

    if firstNum == lastNum:
        return True
    else:
        return False

#create an empty list
inputList = []
#ask number of elements in list
n = int(input("How many items will have the list? "))

#iterating till the range
for i in range(0, n):
    element = float(input(f"Element {i + 1} = "))
    inputList.append(element) #adding element to list

print(f"comparation between first and last element is {first_last_same(inputList)}")

