def get_initials(name: str, surname: str) -> str:
    return f"{name[0].upper()}.{surname[0].upper()}."


def count_letters(text: str, letter: str = "a") -> int:
    """Повертає кількість входжень letter у text без урахування регістру."""
    return text.lower().count(letter.lower())


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count


def reverse_text(text: str) -> str:
    result = ""
    for ch in text:
        result = ch + result
    return result


name = "Yaroslav"
surname = "Korolchuk"
c = 9

print(f"{name} {surname}")
print(get_initials(name, surname))

vowels_count = count_vowels(surname)
consonants_count = c - vowels_count

print(f"Довжина прізвища: {c}")
print(f"Кількість голосних: {vowels_count}")
print(f"Кількість приголосних: {consonants_count}")

for vowel in "aeiou":
    print(f"{vowel}: {count_letters(surname, letter=vowel)}")

print(count_letters(surname))

print(reverse_text(surname))

print(count_letters.__doc__)
print(count_letters.__annotations__)