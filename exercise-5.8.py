floor = int(input("Введите номер этажа: "))
message: str = "Error!"

match floor:
    case -1:
        message = "Подвал: здесь находится склад."
    case 1:
        message = "Hall Reception."
    case 10:
        message = "Технический этаж - вход запрещен."
    case _ if 2 <= floor <= 9:
        if floor % 2 == 0:
            message = "Офисный этаж."
        else:
            message = "Жилой этаж."
    case _:
        message = "Такого этажа нет."

print(message)
