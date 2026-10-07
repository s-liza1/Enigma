alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Зчитуємо вхідні параметри від платформи
operation = input()
shift0 = int(input())
rotor0 = input()
rotor1 = input()
rotor2 = input()
message = input()

#Блок шифрування
if operation == "ENCODE":
    step1 = ""
    after_rotor0 = ""
    after_rotor1 = ""
    after_rotor2 = ""

    # Крок 1: прогресивний зсув Цезаря
    for letter in message:
        old_index = alphabet.find(letter)
        new_index = (old_index + shift0) % 26
        step1 = step1 + alphabet[new_index]
        shift0 = shift0 + 1

    # Крок 2: прохід через ротор 0
    for letter in step1:
        index = alphabet.find(letter)
        step2 = rotor0[index]
        after_rotor0 = after_rotor0 + step2

    # Крок 3: прохід через ротор 1
    for letter in after_rotor0:
        index = alphabet.find(letter)
        step3 = rotor1[index]
        after_rotor1 = after_rotor1 + step3

    # Крок 4: прохід через ротор 2
    for letter in after_rotor1:
        index = alphabet.find(letter)
        step4 = rotor2[index]
        after_rotor2 = after_rotor2 + step4

    print(after_rotor2)

#Блок розшифрування
else:
    before_rotor2 = ""
    before_rotor1 = ""
    before_rotor0 = ""
    final_message = ""

    # Зворотний прохід: спочатку rotor2 -> alphabet
    for letter in message:
        index = rotor2.find(letter)
        step2 = alphabet[index]
        before_rotor2 = before_rotor2 + step2

    # rotor1 -> alphabet
    for letter in before_rotor2:
        index = rotor1.find(letter)
        step1 = alphabet[index]
        before_rotor1 = before_rotor1 + step1

    # rotor0 -> alphabet
    for letter in before_rotor1:
        index = rotor0.find(letter)
        step0 = alphabet[index]
        before_rotor0 = before_rotor0 + step0

    # Скасування зсуву Цезаря
    for letter in before_rotor0:
        index = alphabet.find(letter)
        new_index = (index - shift0) % 26
        step = alphabet[new_index]
        final_message = final_message + step
        shift0 = shift0 + 1

    print(final_message)
