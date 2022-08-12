# 47. Написати програму, яка обчислює, скільки повинен заплатити водій за паркування автомобіля на стоянці протягом певного часу. 
# Користувач вводить наступні дані: час заїзду на стоянку(у годинах і хвилинах), час від’їзду, вартість однієї години паркування. 
# Водій платить за кожну повну годину. Також, здійснюється плата за перевищення користування стоянкою більше ніж на 10 хв., наприклад: 
#     якщо хтось використав стоянку протягом 2 год. і 15 хв., то повинен заплатити за 3 год. 
#     В кінцевому результаті на екран необхідно вивести повідомлення про час заїзду та виїзду авто, ціну за годину паркування і повну вартість.
from datetime import datetime

def parking():
    t_arrive_h, t_arrive_m, t_departure_h, t_departure_m, hour_cost = map(int, input(
        "Input time (hours and minutes) of arrival, time of deparure, cost of one hour: ").split())
    time_arrive = datetime.strptime(f"{t_arrive_h}:{t_arrive_m}", "%H:%M")
    time_departure = datetime.strptime(f"{t_departure_h}:{t_departure_m}", "%H:%M")
    hours = round(((time_departure - time_arrive).total_seconds() / 3600), 3)
    rem = hours - int(hours)
    if rem > 0.167:
        hours += 1
    cost = int(hours) * hour_cost
    check = f"Time of arrival: {t_arrive_h}:{t_arrive_m}\nTime of departure: {t_departure_h}:{t_departure_m}\nCost of one hour: {hour_cost}\nOverall cost: {cost}"
    return check

print(parking())
