# Задача: Счастливый билет
# Серийный номер билета на автобус - это шестизначное число, например 432190.
# Счастливым билетом считается билет, у которого сумма первых трех цифр серийного номера равна
# сумме последних трех цифр.
#
# Функция is_lucky_ticket проверяет, является ли билет счастливым. Она принимает один аргумент
# ticket_id (int) - серийный номер билета, и возвращает True, если билет счастливый,
# и False в противном случае.
#
# В функции также реализованы проверки на корректность входных данных:
# - ticket_id должен быть целым числом.
# - ticket_id должен быть шестизначным.

def is_lucky_ticket(ticket_id: int) -> bool:
    """
    Проверяет, является ли билет счастливым.

    :param ticket_id: Серийный номер билета (должен быть шестизначным целым числом).
    :return: True, если билет счастливый (сумма первых трех цифр равна сумме последних трех цифр), иначе False.
    :raises TypeError: Если ticket_id не является целым числом.
    :raises ValueError: Если ticket_id не является шестизначным числом.
    """

    # Проверка типа ticket_id
    if not isinstance(ticket_id, int):
        raise TypeError(f"Ожидается тип int, но получен {type(ticket_id).__name__}")

    # Преобразуем ticket_id в строку для дальнейшей обработки
    ticket_str = str(ticket_id)

    # Проверка на шестизначность
    if len(ticket_str) != 6:
        raise ValueError("Серийный номер билета должен содержать ровно 6 цифр.")

    # Вычисляем суммы первых и последних трех цифр
    first_half_sum = sum(int(digit) for digit in ticket_str[:3])
    second_half_sum = sum(int(digit) for digit in ticket_str[3:])

    # Сравниваем суммы и возвращаем результат
    return first_half_sum == second_half_sum


# Пример использования функции
try:
    # Вводим серийный номер билета
    ticket_number = int(input("Введите серийный номер билета (6 цифр): "))
    result = is_lucky_ticket(ticket_number)          # Проверяем билет
    print("Счастливый билет!" if result else "Не счастливый билет.")
except ValueError as e:
    print(f"Ошибка: {e}")
except TypeError as e:
    print(f"Ошибка: {e}")
