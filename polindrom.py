word = input("Введите слово палиндром: ").lower()
invert_word = word[::-1]

if word == invert_word:
    print("Строка палиндром")
else:
    print("Строка не является палиндромом")
