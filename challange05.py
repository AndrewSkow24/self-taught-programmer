# Практикум
# 1. Создайте список ваших любимых музыкантов.
favorite_musicians = ["Beatles", "Lumen", "Nirvana"]
print("favorite musicians:", favorite_musicians)
# 2. Создайте список кортежей, где каждый кортеж содержит долготу и широту
# любого места, в котором вы жили или которое посещали.
my_favorite_places = [
    (36.6895, 139.692),  # Токио
    (54.12, 37.37),  # Тула
    (48.50, 2.20),  # Париж
    (51.30, 0.07),  # Лондон
    (41.5400, 12.3000),  # Рим
]
print("favorite places: ", my_favorite_places)

# 3. Создайте словарь, содержащий различные данные о вас: рост, любимый
# цвет, любимый актер и т.д.
about_me = {
    "heigh": 174,
    "color": "red",
    "favorite_actor": "Johny Depp",
    "favorite_musicians": favorite_musicians,
}
print("about me:", about_me)

# 4. Напишите программу, которая запрашивает у пользователя его вес, люби-
# мый цвет или актер, и возвращает результат из словаря, созданного в преды-
# дущем задании.
user_height = int(input("What is your height in sm: "))
user_color = input("What is your favorite color: ")
user_actor = input("What is your facorire actour: ")

user_dict = {"height": user_height, "color": user_color, "favorite_actor": user_actor}

print("Данные о пользователе: ", user_dict)

# 5. Создайте словарь, связывающий ваших любимых музыкантов со списком ва-
# ших любимых песен, написанных ими.
musicians_and_songs = {
    favorite_musicians[0]: ["Let it be", "Yesterday", "And I love her"],
    favorite_musicians[1]: ["Государство", "Синяя птица", "Тень", "Хватит"],
    favorite_musicians[2]: ["Something in the way", "Polly", "All appologies"],
}
print(musicians_and_songs)


# 6. Списки, кортежи и словари — лишь некоторые из встроенных в Python кон-
# тейнеров. Самостоятельно изучите множества (тип контейнеров). В каком
# случае бы вы использовали множество?

my_set = set([1, 1, 2, 2, 3, 2, 5])
print("Множество: ", my_set)

"""
Множества применяются когда каждый элемент последовательности должен быть уникальным
"""
