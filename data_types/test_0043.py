# 43. З міста А в місто Б їде велосипедист. З його плеча злітає муха. Вона летить до міста Б, долітає до нього та повертається назад.
# Знову долітає до велосипедиста, розвертається і летить до міста Б... і так до тих пір, поки велосипедист не доїде до пункту Б.
# Відомо відстань між містами, швидкість велосипедиста та швидкість мухи. Написати програму, що визначає скільки кілометрів налітає муха.

def fly_distance(distance, speed_b, speed_fly):
    time = distance / speed_b
    fly_dis = time * speed_fly
    return round(fly_dis, 2)


print(fly_distance(600, 20, 10))
print(fly_distance(300, 15, 20))
print(fly_distance(60, 14, 15))
print(fly_distance(35, 12, 7))