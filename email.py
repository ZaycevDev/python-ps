email = input("Введите email: ").lower().strip()

if email.count("@") != 1:
    print("Нет1")
    exit()

local, domain = email.split("@")

if not local:
    print("Нет2")
    exit()

if "." not in domain:
    print("Нет3")
    exit()

domain_list = domain.split(".")

if len(domain_list[-1]) < 2:
    print("Нет4")
    exit()

if not domain_list[-2]:
    print("Нет5")
    exit()

print("Да")
