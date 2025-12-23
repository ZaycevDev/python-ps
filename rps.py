import random

CHOICE_RPS = ("камень", "ножницы", "бумага")


def input_user(is_replay: bool) -> str:
    return input(f"Введите {"снова " if is_replay else ""}камень/ножницы/бумага: ").lower()


def user_selects_option():
    user_select = input_user(False)

    while user_select not in CHOICE_RPS:
        print("Не корректный выбор")
        user_select = input_user(True)

    return user_select


def rounds_game(count: int):
    user_points = 0
    comp_points = 0

    for round in range(count):
        print(f"Раунд № {round + 1}")

        user_select = user_selects_option()
        comp = random.choice(CHOICE_RPS)
        print(f"Я выбрал: {comp}")

        if user_select == comp:
            print("В этом раунде ничья")
        elif (user_select == "камень" and comp == "ножницы") or\
            (user_select == "ножницы" and comp == "бумага") or\
                (user_select == "бумага" and comp == "камень"):
            print("В этом раунде победа за вами!")
            user_points += 1
        else:
            print("В этом раунде победа за мной")
            comp_points += 1

    return (user_points, comp_points)


def Game():
    print("Привет! Давай сыграем в игру камень, ножницы, бумага.")

    count_round = "0"

    while not count_round.isnumeric() or int(count_round) < 1:
        count_round = input("Сколько раундов со мной хочешь сыграть?: ")

    (user_points, comp_points) = rounds_game(int(count_round))

    if user_points > comp_points:
        print("По итогам всех раундов Вы выиграли.")
    elif user_points == comp_points:
        print("По итогам всех раундов ничья.")
    else:
        print("По итогам всех раундов Вы проиграли")


Game()
