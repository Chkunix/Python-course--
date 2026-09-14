def read_grade(prompt):
    """Запитує в користувача ціле число від 0 до 100 і повертає його."""
    while True:
        raw = input(prompt)
        try:
            grade = int(raw)
        except ValueError:
            print("Помилка: потрібно ввести ціле число.")
            continue
        if grade < 0 or grade > 100:
            print("Помилка: оцінка повинна бути в межах від 0 до 100.")
            continue
        return grade


def to_letter(grade):
    """Повертає буквену оцінку (A-F) для числової оцінки grade."""
    if grade >= 90:
        return "A"
    if grade >= 80:
        return "B"
    if grade >= 70:
        return "C"
    if grade >= 60:
        return "D"
    return "F"


def average(grades):
    """Повертає середнє арифметичне списку оцінок grades."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Повертає кількість оцінок у grades, більших за limit."""
    count = 0
    for grade in grades:
        if grade > limit:
            count += 1
    return count


def print_report(name, group, grades):
    """Друкує звіт про оцінки студента: список, середнє, буквену оцінку,
    найкращий і найгірший бали, кількість оцінок вище середнього."""
    avg = average(grades)
    letter = to_letter(avg)
    above_avg = count_above(grades, avg)

    print(f"Студент: {name}")
    print(f"Група: {group}")
    print(f"Оцінки: {grades}")
    print(f"Середнє: {avg:.2f} ({letter})")
    print(f"Найкращий бал: {max(grades)}")
    print(f"Найгірший бал: {min(grades)}")
    print(f"Оцінок вище середнього: {above_avg}")


def main():
    """Головна функція: збирає оцінки студента і друкує звіт."""
    name = "Yaroslav"
    group = "IT-31"
    n = 8

    grades = []
    for i in range(n):
        grade = read_grade(f"Введіть оцінку {i + 1}/{n}: ")
        grades.append(grade)

    print_report(name, group, grades)


main()