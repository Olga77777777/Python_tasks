"""
Импорт модуля calculator
"""


import calculator


# Запрос данных у пользователя
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Выберите операцию (+, -, *, /): ")

# Выполнение операции
if operation == "+":
    result = calculator.add(a, b)
elif operation == "-":
    result = calculator.subtract(a, b)
elif operation == "*":
    result = calculator.multiply(a, b)
elif operation == "/":
    result = calculator.divide(a, b)
else:
    result = "Ошибка: неизвестная операция!"

print(f"Результат: {result}")