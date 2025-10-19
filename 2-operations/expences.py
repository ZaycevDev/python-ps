food = float(input("Введите траты на еду: "))
transport = float(input("Введите траты на транспорт: "))
entertainment = float(input("Введите траты на развлечения: "))
sum_total = food + transport + entertainment

print(f"Общая сумма трат: {sum_total}")
print(f"Средняя сумма трат: {sum_total / 3}")
