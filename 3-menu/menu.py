"""Module providing a function printing python version."""
import sys

DRINK = "напиток"
SOUP = "суп"
DESSERT = "десерт"

dish: str = "не выбрано"
price: float

menu_category = input(
    "Введите категорию блюд (напиток, суп, десерт): ").lower()


if menu_category == DRINK:
    dish = input("Выберете напиток (чай, кофе, сок): ").lower()
elif menu_category == SOUP:
    dish = input("Выберете суп (борщ, щи, суп-пюре): ").lower()
elif menu_category == DESSERT:
    dish = input("Выберете десерт (торт, мороженное, фрукты): ").lower()
else:
    print("Введено неверное блюдо")
    sys.exit()

match dish:
    case "чай":
        price = 1.0
    case "кофе":
        price = 2.0
    case "сок":
        price = 3.0
    case "борщ":
        price = 10.0
    case "щи":
        price = 11.0
    case "суп-пюре":
        price = 12.0
    case "торт":
        price = 20.0
    case "мороженное":
        price = 21.0
    case "фрукты":
        price = 22.0
    case _:
        price = 0.0

print(f"Цена: {price} руб.")
