import sys
import math#Kango911

class Menu:
    @staticmethod
    def display_menu():
        print(f"\n\nВыполнил Группа: <Kango911>")
        print("Это консольное приложение является калькулятором для систем счисления от 1 до 50 включительно, а также служит калькулятором для перевода чисел в римскую СС.\n\n")
        print("Выберите что вы хотите сделать:")
        print("1. Перевести из одной системы счисления в другую.")
        print("2. Перевести число из Арабской в Римскую и наоборот.")
        print("3. Сложение в произвольной системе счисления")
        print("4. Вычитание в произвольной системе счисления")
        print("5. Умножение в произвольной системе счисления")
        print("Все действия необходимо подтверждать нажатием клавиши Enter.")
        choice = input()
        if choice == '1':
            ConvertingToAnyBase.transfer_to_another_system()
            Menu.return_to_menu()
        elif choice == '2':
            ArabicOrRomanian.choose_the_system()
            Menu.return_to_menu()#Kango911
        elif choice == '3':
            SummaryInAnySystem.summary()
            Menu.return_to_menu()
        elif choice == '4':
            SubtractionInAnySystem.subtraction()
            Menu.return_to_menu()
        elif choice == '5':#Kango911
            MultiplicationInAnySystem.multiplication()
            Menu.return_to_menu()

    @staticmethod
    def return_to_menu():
        print("Хотите ли вы еще воспользоваться программой?")
        print("Если хотите то введите 1.")
        print("Иначе введите что угодно.")
        choice = input()
        if choice == '1':
            print("", end='')#Kango911
            Menu.display_menu()
        else:
            sys.exit()

class ConvertingToAnyBase:
    numbers = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 21: 'K', 22: 'L',
               23: 'M', 24: 'N', 25: 'O', 26: 'P', 27: 'Q', 28: 'R', 29: 'S', 30: 'T', 31: 'U', 32: 'V', 33: 'W', 34: 'X',
               35: 'Y', 36: 'Z', 37: 'a', 38: 'b', 39: 'c', 40: 'd', 41: 'e', 42: 'f', 43: 'g', 44: 'h', 45: 'i', 46: 'j',
               47: 'k', 48: 'l', 49: 'm', 50: 'n'}#Kango911

    @staticmethod
    def convert_from_dec(num, base):
        result = ''
        pos = num
        while True:
            if pos == 1:
                result += str(pos)
                break
            elif pos == 0:#Kango911
                break
            remainder = pos % base
            if remainder > 9:
                result += ConvertingToAnyBase.numbers[remainder]
            else:
                result += str(remainder)
            pos //= base
        return ConvertingToAnyBase.reverse(result)

    @staticmethod
    def convert_to_dec(num, base):#Kango911
        result = 0
        s = 0
        for i in range(len(num) - 1, -1, -1):
            result += int(math.pow(base, s)) * int(num[i])
            s += 1
        return result

    @staticmethod
    def transfer_to_another_system():
        print("", end='')
        print("Введите число:")
        number = input()
        print("", end='')
        print("Введите систему счисления:")
        system = int(input())#Kango911
        if int(number) <= 0 or system <= 0:
            print("", end='')
            print("Введите число больше нуля!")
            print("Для продолжения нажмите любую кнопку.")
            input()
            ConvertingToAnyBase.transfer_to_another_system()
        else:
            verification = int(number)
            while verification > 0:
                check = verification % 10
                if check >= system:
                    print("", end='')
                    print("Вы ввели неправильное число. Число не должно содержать цифр больше или равных значению системы счисления.")
                    print("Для продолжения нажмите любую кнопку.")
                    input()
                    ConvertingToAnyBase.transfer_to_another_system()#Kango911
                verification //= 10
        print("", end='')
        tru_num = list(number)
        print(f"Берем последний элемент числа(в данном случае {tru_num[-1]})")
        print(f"И умножаем его ({tru_num[-1]}) на систему счисления (в данном случае {system}) в степени начиная с 0")
        ans = int(tru_num[-1]) * int(math.pow(system, 0))
        print(f"В данном случае ответ будет {ans}")
        print("Дальше берем следующий элемент и домножаем на систему счисления в степени на 1 больше.")
        print(f"В конце складываем полученные результаты и получаем ответ(в десятичной системе):{ConvertingToAnyBase.convert_to_dec(tru_num, system)}")
        print("Для продолжения нажмите любую кнопку.")
        input()
        print("", end='')
        print("Введите в какую систему счисления осуществить перевод:")#Kango911
        sys2 = int(input())
        if sys2 <= 0:
            print("", end='')
            print("Введите число больше нуля!")
            print("Для продолжения нажмите любую кнопку.")
            input()#Kango911
            ConvertingToAnyBase.transfer_to_another_system()
        else:
            print("", end='')
            result = ConvertingToAnyBase.convert_from_dec(ConvertingToAnyBase.convert_to_dec(tru_num, system), sys2)
            print(f"Ответ в {sys2}-ой системе: {result}")

    @staticmethod
    def reverse(line):
        return line[::-1]

class ArabicOrRomanian:#Kango911
    @staticmethod
    def choose_the_system():
        print("", end='')
        print("Нажмите 1, если хотите перевести арабские цифры в римские")
        print("Нажмите 2, если хотите перевести римские цифры в арабские")
        choice = int(input())
        if choice == 1:
            print(ArabicOrRomanian.arabic_to_roman(ArabicOrRomanian.arabic_input()))
        elif choice == 2:#Kango911
            print(ArabicOrRomanian.roman_to_arabic(ArabicOrRomanian.roman_input()))
        else:
            print("", end='')
            print("Вы ввели неправильное значение.")
            print("Для продолжения нажмите любую клавишу.")
            input()
            ArabicOrRomanian.choose_the_system()

    @staticmethod
    def arabic_input():
        print("Введите число, которое хотите перевести")#Kango911
        arabic = int(input())
        print("", end='')
        return arabic

    @staticmethod
    def arabic_to_roman(arabic_number):
        if arabic_number > 5000:
            print("Число превышает максимально допустимое значение, пожалуйста введите новое число меньше или равное 5000")
            arabic_number = int(input())
            print("", end='')
            return ArabicOrRomanian.arabic_to_roman(arabic_number)
        else:
            thousands = ["", "M", "MM", "MMM", "MMMM", "MMMMM"]
            hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
            tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]#Kango911
            ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

            result = ''
            result += thousands[arabic_number // 1000]
            arabic_number %= 1000
            result += hundreds[arabic_number // 100]
            arabic_number %= 100
            result += tens[arabic_number // 10]
            arabic_number %= 10
            result += ones[arabic_number]

            return result

    # Kango911
    def roman_input():
        print("Введите римское значение числа:")
        roman = input()
        print("", end='')
        return roman

    @staticmethod
    def roman_to_arabic(roman):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman = roman.upper()
        total = 0
        last_value = 0
        for char in roman[::-1]:
            value = roman_dict.get(char, 0)#Kango911
            if value >= last_value:
                total += value
            else:
                total -= value
            last_value = value
        return total

class SummaryInAnySystem:#Kango911
    @staticmethod
    def summary():
        print("", end='')
        print("Введите первое число:")
        number1 = input()
        print("", end='')
        print("Введите второе число:")
        number2 = input()
        print("", end='')
        print("Введите систему счисления:")
        system = int(input())
        print("", end='')
        if system <= 0:#Kango911
            print("Введите систему счисления больше нуля!")
            print("Для продолжения нажмите любую кнопку.")
            input()
            SummaryInAnySystem.summary()
        else:
            num1 = ConvertingToAnyBase.convert_to_dec(number1, system)
            num2 = ConvertingToAnyBase.convert_to_dec(number2, system)
            result = num1 + num2
            print(f"Их сумма в {system}-ой системе: {ConvertingToAnyBase.convert_from_dec(result, system)}")

class SubtractionInAnySystem:
    @staticmethod#Kango911
    def subtraction():
        print("", end='')
        print("Введите первое число:")
        number1 = input()
        print("", end='')
        print("Введите второе число:")
        number2 = input()
        print("", end='')
        print("Введите систему счисления:")
        system = int(input())
        print("", end='')
        if system <= 0:
            print("Введите систему счисления больше нуля!")
            print("Для продолжения нажмите любую кнопку.")
            input()
            SubtractionInAnySystem.subtraction()#Kango911
        else:
            num1 = ConvertingToAnyBase.convert_to_dec(number1, system)
            num2 = ConvertingToAnyBase.convert_to_dec(number2, system)#Kango911
            if num1 < num2:
                print("Первое число должно быть больше второго!")
                print("Для продолжения нажмите любую кнопку.")
                input()
                SubtractionInAnySystem.subtraction()
            else:
                result = num1 - num2
                print(f"Их разность в {system}-ой системе: {ConvertingToAnyBase.convert_from_dec(result, system)}")

class MultiplicationInAnySystem:
    @staticmethod
    def multiplication():
        print("", end='')
        print("Введите первое число:")
        number1 = input()
        print("", end='')#Kango911
        print("Введите второе число:")
        number2 = input()
        print("", end='')
        print("Введите систему счисления:")
        system = int(input())
        print("", end='')
        if system <= 0:
            print("Введите систему счисления больше нуля!")
            print("Для продолжения нажмите любую кнопку.")#Kango911
            input()
            MultiplicationInAnySystem.multiplication()
        else:
            num1 = ConvertingToAnyBase.convert_to_dec(number1, system)
            num2 = ConvertingToAnyBase.convert_to_dec(number2, system)
            result = num1 * num2
            print(f"Их произведение в {system}-ой системе: {ConvertingToAnyBase.convert_from_dec(result, system)}")

if __name__ == "__main__":
    Menu.display_menu()#Kango911
