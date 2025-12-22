# Практикум
# 1. Напишите функцию, которая принимает число в качестве ввода, возводит
# его в квадрат и возвращает.


def square(num):
    """
    :param num: int or float
    :return: square of num (int or float)
    """
    return num**2


print(square(2))

# 2. Создайте функцию, которая принимает строку в качестве параметра и воз-
# вращает ее.


def return_str(str):
    """
    :param str: str
    :return: param str
    """
    return str


print(return_str("string"))


# 3. Напишите функцию, которая принимает три обязательных и два необяза-
# тельных параметра.


def three_nums(num1, num2, num3, operation="+", to_int=False):
    """
    Функция принимает 3 обязательных параметра - 3 числа, по умолчанию их
    складывает, но можно задать вычитание, умножение или деление.
    5 параметр служит для приведения к целочисленному типу
    :param num1: int or float
    :param num2: int or float
    :param num3: int or float
    :param operation: str + or - or * or /
    :param to_int: bool
    :return: int or float
    """
    if to_int:
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)

    if operation == "+":
        return num1 + num2 + num3
    elif operation == "-":
        return num1 - num2 - num3
    elif operation == "*":
        return num1 * num2 * num3
    elif operation == "/":
        if to_int:
            return num1 // num2 // num3
        return num1 / num2 / num3
    else:
        return None


print(three_nums(1, 2, 3))
print(three_nums(1, 2, 3, "/"))
print(three_nums(1, 2, 3, "/", True))
print(three_nums(1, 2, 3, "%"))
print(
    three_nums(
        1.9,
        2.3,
        3.5,
        "/",
    )
)


# 4. Напишите программу с двумя функциями. Первая функция должна при-
# нимать в качестве параметра целое число и возвращать результат деления
# этого числа на 2. Вторая функция должна принимать в качестве параметра
# целое число и возвращать результат умножения этого числа на 4. Вызовите
# первую функцию, сохраните результат в переменной и передайте ее в каче-
# стве параметра во вторую функцию.


def div2(num):
    """
    :param num: int
    :return: num / 2 : float
    """
    return num / 2


def mult4(num):
    """
    :param num: float or int
    :return: num * 4: float or int
    """
    return num * 4


result = div2(100)
print(mult4(result))


# 5. Напишите функцию, которая преобразовывает строку в тип данных float и
# возвращает результат. Используйте обработку исключений, чтобы перехва-
# тить возможные исключения.
def str_to_float(str):
    """
    :param str: str with nums and point
    :return: float num
    """

    try:
        result = float(str)
        return result
    except Exception:
        print("Something went wrong")


print(str_to_float("1234.5"))
print(str_to_float("one two"))

# 6. Добавьте строку документации ко всем функциям, которые вы написали в за-
# даниях 1–5.
