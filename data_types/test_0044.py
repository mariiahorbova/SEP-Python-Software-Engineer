# 44.Написати програму, яка визначає дату наступного дня, на основі сьогоднішньої дати.
import datetime

# 1 version - user input "day month"
def tomorrow():
    day, month = map(int, input("Input day and month: ").split())
    date = datetime.date(2022, month, day) + datetime.timedelta(days=1)
    return date.strftime('%d %B')
    
print(tomorrow())


# 2 version - automatic
def day_after_today():
    today = datetime.date.today()
    tomorrow = (today + datetime.timedelta(days=1)).strftime('%d %B')
    return tomorrow

print(day_after_today())
