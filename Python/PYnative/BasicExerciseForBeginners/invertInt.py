#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

numberOrigin = int(input("Type a integer number: "))

while numberOrigin > 0:
    digit = numberOrigin % 10 #get the last digit
    numberOrigin = numberOrigin // 10 #remove the last digit and repeat the loop
    print(f"{digit}", end=" ")