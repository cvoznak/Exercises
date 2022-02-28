# Exercise 1: Calculate the multiplication and sum of two numbers
print("Given two integer numbers return their product only if the product is greater than 1000, else return their sum.")


# Function definition num1 and num2 are parameters
def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product > 1000:
        return product
    else:
        return num1 + num2


# Input from user
num1 = int(input("number1 = "))
num2 = int(input("number2 = "))


# Apply function and return result
result = multiplication_or_sum(num1, num2)
print(f"The result is {result}")
