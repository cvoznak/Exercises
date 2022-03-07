#Exercise 9: Check Palindrome Number

number = input("Original number to check:")

reverseNumber = number[::-1]#slice in reverse

if number == reverseNumber:
    print("Yes, given number is a palindrome number.")
else:
    print("No, given number is not palindrome number.")


