#Exercise 8: Print the following pattern

nLines = int(input("How many lines do you wish?"))

for i in range(0, (nLines + 1)):
    print(f"{(str(i) + str(' ')) * i}")

#Another option is:

#for num in range(nLines + 1):
    #for i in range(num):
        #print(num, end=" ")
    #print("\n")