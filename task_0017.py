# 17. Write a Python program to check if a number is within 10 of 100 or 200. (E.g. 90, 110, 190, 210)

def check_within_10(num):
    return abs(num - 100) <= 10 or abs(num - 200) <= 10

print(check_within_10(90))
print(check_within_10(110))
print(check_within_10(190))
print(check_within_10(210))
print(check_within_10(9))
print(check_within_10(80))
print(check_within_10(150))
