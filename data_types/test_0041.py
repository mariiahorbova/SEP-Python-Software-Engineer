# 41. Write a Python program to check three given integers x, y, z 
# and return true if one of y or z is close(differing from a by at most 1), 
# while the other is far, differing from both other values by 3 or more.


def check_xyz(x, y, z):
    if abs(y - z) < 3:
        return False
    return (abs(x - y) <= 1 and abs(x - z) >= 3) or (abs(x - z) <= 1 and abs(x - y) >= 3)

print(check_xyz(7, 8, 13))
print(check_xyz(5, 4, 75))
print(check_xyz(1, 2, 3))
