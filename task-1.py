from datetime import datetime

def get_days_from_today(date: str) -> int | str:
    try:
        #  Перетворюємо рядок дати на об'єкт datetime
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        # Отримання поточної дати
        current_date = datetime.today()
        # Розраховуємо різницю між датами
        difference = current_date - date_obj
        # Повертаємо кількість днів (може бути від'ємним, якщо дата в майбутньому)
        return difference.days
    except ValueError:
        # Повертаємо повідомлення про помилку для неправильного формату дати
        return "Invalid date format. Enter date in 'YYYY-MM-DD' format."
    
print(get_days_from_today('1984-09-06'))





  
