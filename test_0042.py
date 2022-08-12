# 42. На зустріч один одному відповідно з міста А та міста Б рухається заєць та черепаха.
# Ввести з клавіатури відстань між містами, швидкість зайця та швидкість черепахи.
# Обчислити на якій відстані від міста Б вони зустрінуться.

def distance(dis, speed_h, speed_t):
    v = speed_h + speed_t
    t = dis / v
    dis_to_B = t * speed_t
    return dis_to_B


print(distance(36, 10, 8))
print(distance(350, 30, 20))
print(distance(90, 19, 7))
