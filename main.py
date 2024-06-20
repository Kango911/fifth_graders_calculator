class Converter:
    numbers = {
        10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I", 19: "J", 20: "K", 21: "L",
        22: "M", 23: "N", 24: "O", 25: "P", 26: "Q", 27: "R", 28: "S", 29: "T", 30: "U", 31: "V", 32: "W", 33: "X",
        34: "Y", 35: "Z", 36: "a", 37: "b", 38: "c", 39: "d", 40: "e", 41: "f", 42: "g", 43: "h", 44: "i", 45: "j",
        46: "k", 47: "l", 48: "m", 49: "n"
    }

    @staticmethod
    def convert_from_dec(num, sys):
        result = ""
        pos = num
        while True:
            if pos == 1:
                result += str(pos)
                break
            elif pos == 0:
                break
            ost = pos % sys
            if ost > 9:
                result += Converter.numbers[ost]
            else:
                result += str(ost)
            pos //= sys
        return result[::-1]

    @staticmethod
    def convert_to_dec(num, sys):
        result = 0
        s = 0
        for i in range(len(num) - 1, -1, -1):
            result += int(num[i]) * (sys ** s)
            s += 1
        return result


class ArabicOrRomanian:
    char_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    @staticmethod
    def arabic_to_romanian(arabic_number):
        if arabic_number > 5000:
            print(
                "Число превышает максимально допустимое значение, пожалуйста введите новое число меньше или равное 5000")
            arabic_number = int(input())
            return ArabicOrRomanian.arabic_to_romanian(arabic_number)
        else:
            thousands = ["", "M", "MM", "MMM", "MMMM", "MMMMM"]
            hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
            tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
            ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

            result = ""
            result += thousands[arabic_number // 1000]
            arabic_number %= 1000

            result += hundreds[arabic_number // 100]
            arabic_number %= 100

            result += tens[arabic_number // 10]
            arabic_number %= 10

            result += ones[arabic_number]
            return result

    @staticmethod
    def romanian_to_arabic(roman):
        if not roman:
            return 0
        roman = roman.upper()

        if roman[0] == '(':
            pos = roman.rindex(')')
            part1 = roman[1:pos]
            part2 = roman[pos + 1:]
            return 1000 * ArabicOrRomanian.romanian_to_arabic(part1) + ArabicOrRomanian.romanian_to_arabic(part2)

        total = 0
        last_value = 0
        for i in range(len(roman) - 1, -1, -1):
            new_value = ArabicOrRomanian.char_values[roman[i]]
            if new_value < last_value:
                total -= new_value
            else:
                total += new_value
                last_value = new_value
        return total


class Menu:
    @staticmethod
    def display_menu():
        print(
            "     Это консольное приложение является калькулятором для систем счисления от 1 до 50 включительно, а также служит калькулятором для перевода чисел в римскую СС.")
        print("     Выполнил Lipenkov A.D. Группа: ПрИ-101")
        print("Выберите что вы хотите сделать:")
        print("1. Перевести из одной системы счисления в другую.")
        print("2. Перевести число из Арабской в Римскую и наоборот.")
        print("3. Сложение в произвольной системе счисления")
        print("4. Вычитание в произвольной системе счисления")
        print("5. Умножение в произвольной системе счисления")
        print("Все действия необходимо подтверждать нажатием клавиши Enter.")
        choice = input()
        if choice == "1":
            Menu.convert_between_bases()
        elif choice == "2":
            Menu.arabic_roman_conversion()
        elif choice == "3":
            Menu.perform_addition()
        elif choice == "4":
            Menu.perform_subtraction()
        elif choice == "5":
            Menu.perform_multiplication()

    @staticmethod
    def convert_between_bases():
        print("Введите число:")
        number = input()
        print("Введите систему счисления:")
        system = int(input())

        verification = int(number)
        while verification > 0:
            if verification % 10 >= system:
                print(
                    "Вы ввели неправильное число. Число не должно содержать цифр больше или равных значению системы счисления.")
                return Menu.convert_between_bases()
            verification //= 10

        num_in_base = Converter.convert_to_dec(number, system)
        print(f"Введите в какую систему счисления осуществить перевод:")
        target_base = int(input())
        converted = Converter.convert_from_dec(num_in_base, target_base)
        print(f"Ответ в {target_base}-ой системе: {converted}")

    @staticmethod
    def arabic_roman_conversion():
        print("Нажмите 1, если хотите перевести арабские цифры в римские")
        print("Нажмите 2, если хотите перевести римские цифры в арабские")
        choice = int(input())
        if choice == 1:
            print("Введите число, которое хотите перевести")
            arabic = int(input())
            print(ArabicOrRomanian.arabic_to_romanian(arabic))
        elif choice == 2:
            print("Введите римское значение числа:")
            roman = input()
            print(ArabicOrRomanian.romanian_to_arabic(roman))
        else:
            print("Вы ввели неправильное значение.")
            return Menu.arabic_roman_conversion()

    @staticmethod
    def perform_addition():
        print("Введите первое число:")
        number1 = input()
        print("Введите второе число:")
        number2 = input()
        print("Введите систему счисления:")
        system = int(input())

        num1_dec = Converter.convert_to_dec(number1, system)
        num2_dec = Converter.convert_to_dec(number2, system)
        result_dec = num1_dec + num2_dec
        result_base = Converter.convert_from_dec(result_dec, system)
        print(f"Их сумма в {system}-ой системе: {result_base}")

    @staticmethod
    def perform_subtraction():
        print("Введите первое число:")
        number1 = input()
        print("Введите второе число:")
        number2 = input()
        print("Введите систему счисления:")
        system = int(input())

        num1_dec = Converter.convert_to_dec(number1, system)
        num2_dec = Converter.convert_to_dec(number2, system)
        if num1_dec < num2_dec:
            print("Первое число должно быть больше второго!")
            return Menu.perform_subtraction()

        result_dec = num1_dec - num2_dec
        result_base = Converter.convert_from_dec(result_dec, system)
        print(f"Их разность в {system}-ой системе: {result_base}")

    @staticmethod
    def perform_multiplication():
        print("Введите первое число:")
        number1 = input()
        print("Введите второе число:")
        number2 = input()
        print("Введите систему счисления:")
        system = int(input())

        num1_dec = Converter.convert_to_dec(number1, system)
        num2_dec = Converter.convert_to_dec(number2, system)
        result_dec = num1_dec * num2_dec
        result_base = Converter.convert_from_dec(result_dec, system)
        print(f"Их произведение в {system}-ой системе: {result_base}")


if __name__ == "__main__":
    Menu.display_menu()