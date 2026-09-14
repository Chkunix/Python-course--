def print_card():
    print("Ім'я: Ярослав")
    print("Прізвище: Корольчук")
    print("Група: IT-31")
    print("Рік народження: 2009")


print_card()
print_card()
print_card()


def print_card_args(name, surname, group, year):
    print(f"Ім'я: {name}")
    print(f"Прізвище: {surname}")
    print(f"Група: {group}")
    print(f"Рік народження: {year}")


print_card_args("Ярослав", "Корольчук", "IT-31", 2009)

print_card_args(year=2009, name="Ярослав", group="IT-31", surname="Корольчук")

print_card_args("Ярослав", "Корольчук", year=2009, group="IT-31")

def print_card_default(name, surname, year, group="IT-31"):
    print(f"Ім'я: {name}")
    print(f"Прізвище: {surname}")
    print(f"Група: {group}")
    print(f"Рік народження: {year}")


print_card_default("Ярослав", "Корольчук", 2009)