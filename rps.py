import random

CHOICE_RPS = ("камень", "ножницы", "бумага")
print("Привет! Давай сыграем в игру камень, ножницы, бумага.")
count_round = int(input("Сколько раундов со мной хочешь сыграть?: "))
user_points = 0
bot_points = 0

for round in range(count_round):
    print(f"Раунд № {round + 1}")
    user = input("Введите камень/ножницы/бумага: ").lower()

    while user not in CHOICE_RPS:
        print("Не корректный выбор")
        user = input("Введите снова камень/ножницы/бумага: ").lower()

    bot = random.choice(CHOICE_RPS)
    print(f"Я выбрал: {bot}")

    if user == bot:
        print("В этом раунде ничья")
    elif (user == "камень" and bot == "ножницы") or\
        (user == "ножницы" and bot == "бумага") or\
            (user == "бумага" and bot == "камень"):
        print("В этом раунде победа за вами!")
        user_points += 1
    else:
        print("В этом раунде победа за мной")
        bot_points += 1

if user_points > bot_points:
    print("По итогам всех раундов Вы выиграли.")
elif user_points == bot_points:
    print("По итогам всех раундов ничья.")
else:
    print("По итогам всех раундов Вы проиграли")
