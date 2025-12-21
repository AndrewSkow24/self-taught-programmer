try:
    first_num = int(input("first num: "))
    second_num = int(input("second num: "))
    print(first_num / second_num)
except (ZeroDivisionError, ValueError):
    print("You aren't right, something went wrong")
