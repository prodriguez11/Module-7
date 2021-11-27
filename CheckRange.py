# Check the range if the entered number is in range (1,10)
# use if statement with the range
# input Enter a number
# print it is in range if between (1-10)
# print is not in range if not between (1-10)


def checkRange(num):
    if num in range(1,10):
        print("It is in range")
    else:
        print("Not in range")

num = int(input("Enter a number: "))
checkRange(num)