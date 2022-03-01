# Exercise 2: Print the sum of the current number and the previous number

print("Printing current and previous number sum in a range(10)")

n = int(input("Type an integre number: "))
previous = 0

#loop from 0 to 9 (10 steps)
for i in range(0, 10):
    sumTotal = n + previous
    print(f"Current Number {n} Previous Number {previous} Sum: {sumTotal}")
    previous = n
    n += 1

