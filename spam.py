messages = [
    "Привет!",
    "Купи дешёвые курсы!!!",
    "Как дела?",
    "СПАМ реклама!!!",
    "Пойдем играть в футбол?",
]

SPAM = "СПАМ"

for message in messages:
    if len(message) > 20:
        continue

    if SPAM in message:
        print("Есть спам!!!")
        print(f"{message}")
        break

else:
    print("Спама нет!")
