y = 2009


def print_age(year):
    age = 2026 - year
    print(f"Вік: {age}")


def get_age(year, current_year=2026):
    return current_year - year


print_age(y)
print(get_age(y))

print(print_age(y))

age_years = get_age(y)
age_months = age_years * 12
age_weeks = age_years * 52

print(f"Вік у місяцях: {age_months}")
print(f"Вік у тижнях: {age_weeks}")

age_in_2030 = get_age(y, current_year=2030)
print(f"У 2030 році мені буде: {age_in_2030} років")


def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1
    return current_year - year


print(get_age(3000))


def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1
    return current_year - year
    print("after return")


get_age(y)