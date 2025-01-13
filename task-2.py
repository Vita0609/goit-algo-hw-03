import random
def get_numbers_ticket(min_value, max_value, quantity):
    # Перевірка вхідних параметрів
    if not (1 <= min_value <= max_value <= 1000):
        return []
    if not (1 <= quantity <= (max_value - min_value + 1)):
        return []

    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_value, max_value + 1), quantity)

    # Сортування чисел
    return sorted(numbers)

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
