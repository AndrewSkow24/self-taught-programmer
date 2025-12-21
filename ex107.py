a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

try:
    print(a / b)
except ZeroDivisionError:
    print("the second number can't be 0")
