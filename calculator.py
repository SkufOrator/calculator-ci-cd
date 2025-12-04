def calculator():
    print("Доступные операции:")
    print("+ Сложение")
    print("- Вычитание")
    print("* Умножение")
    print("/ Деление")

    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка: Введите корректные числа!")
        return

    result = None

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Ошибка: Деление на ноль!")
            return
    else:
        print("Ошибка: Неверный оператор!")
        return

    print(f"Результат: {result}")


if __name__ == "__main__":
    calculator()