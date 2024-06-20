import numpy as np

def from_base_n_to_base_10(number, base):
    try:
        return int(number, base)
    except ValueError:
        print("Ошибка: Некорректное число для данной системы счисления")
        return None

def from_base_10_to_base_n(number, base):
    try:
        return np.base_repr(number, base)
    except ValueError:
        print("Ошибка: Некорректная база системы счисления")
        return None

def addition(num1, num2, base):
    result = from_base_n_to_base_10(num1, base) + from_base_n_to_base_10(num2, base)
    return from_base_10_to_base_n(result, base)

def subtraction(num1, num2, base):
    result = from_base_n_to_base_10(num1, base) - from_base_n_to_base_10(num2, base)
    if result < 0:
        print("Ошибка: Результат вычитания отрицательный в данной системе счисления")
        return None
    return from_base_10_to_base_n(result, base)

def multiplication(num1, num2, base):
    result = from_base_n_to_base_10(num1, base) * from_base_n_to_base_10(num2, base)
    return from_base_10_to_base_n(result, base)

def division(num1, num2, base):
    try:
        result = from_base_n_to_base_10(num1, base) // from_base_n_to_base_10(num2, base)
        return from_base_10_to_base_n(result, base)
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль")
        return None

# Функция для ввода числа с проверкой на корректность
def input_number(prompt, base):
    while True:
        try:
            number = input(prompt + ": ")
            int(number, base)
            return number
        except ValueError:
            print("Ошибка: Некорректное число для данной системы счисления")

# Функция для перевода числа из одной системы счисления в другую
def convert_number(num, from_base, to_base):
    decimal_num = from_base_n_to_base_10(num, from_base)
    if decimal_num is not None:
        return from_base_10_to_base_n(decimal_num, to_base)
    else:
        return None

# Главный цикл программы
while True:
    print("\nВыберите действие:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Перевод числа из одной системы счисления в другую")
    print("6. Выход")

    choice = input("Введите номер действия: ")

    if choice == "6":
        break
    elif choice in ["1", "2", "3", "4"]:
        base = int(input("Введите базу системы счисления: "))
        num1 = input_number("Введите первое число", base)
        num2 = input_number("Введите второе число", base)

        if choice == "1":
            print("Результат сложения:", addition(num1, num2, base))
        elif choice == "2":
            print("Результат вычитания:", subtraction(num1, num2, base))
        elif choice == "3":
            print("Результат умножения:", multiplication(num1, num2, base))
        elif choice == "4":
            print("Результат деления:", division(num1, num2, base))
    elif choice == "5":
        num = input_number("Введите число", int(input("Введите базу исходной системы счисления: ")))
        to_base = int(input("Введите целевую базу системы счисления: "))
        print("Результат перевода:", convert_number(num, int(input("Введите базу исходной системы счисления: ")), to_base))
    else:
        print("Ошибка: Некорректный выбор действия")
