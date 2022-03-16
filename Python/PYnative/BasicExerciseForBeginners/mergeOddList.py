#Exercise 10: Create a new list from a two list using the following condition
#Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

def mergeOddList(list1, list2):
    resultList = []

    for num in list1:
        if num % 2 != 0:
            resultList.append(num)
    for num in list2:
        if num % 2 != 0:
            resultList.append(num)

    return resultList

list1 = []
list2 = []

n = int(input("How many items will have list1? "))

for i in range(0, n):
    element = float(input("Element:"))
    list1.append(element)

n = int(input("How many items will have list2? "))

for i in range(0, n):
    element = float(input("Element:"))
    list2.append(element)

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"Result = {mergeOddList(list1,list2)}")
