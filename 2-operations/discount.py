price_of_goods = float(input("Напиши цену товара: "))
discount = float(input("Напиши процент скидки: "))
discount_price = price_of_goods * (discount / 100)
print("Ваша скидка " + str(discount_price))
