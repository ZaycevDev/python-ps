spending_list = []
list_of_days = ['понедельник', 'вторник', "среда",
                "четверг", "пятница", "суббота", "воскресение"]
for day in list_of_days:
    waste = int(input(f"Введите свои расходы за {day}: "))
    spending_list.append(waste)

sum_waste = sum(spending_list)
max_waste = max(spending_list)
min_waste = min(spending_list)

tuple_waste = (min_waste, max_waste, sum_waste)
print(tuple_waste)
