colors = ["Фиолетовый", "оранжевый", "зелёный"]

guess = input("Угадайте цвет: ")
guess = guess.lower().strip()

if guess in colors:
    print("Вы угадали")
else:
    print("Неправильно, попробуйте ещё раз")
