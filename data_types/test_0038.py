# 38. Write a Python program to check three given integers and return true if one of them is 20 or more less than one of the others.

def check_three(num1, num2, num3):
    return (abs(num1 - num2) >= 20 or abs(num2 - num3) >= 20 or abs(num3 - num1) >= 20)

print(check_three(8, 30, 25))
print(check_three(20, 35, 34))
print(check_three(9, 50, 54))
print(check_three(35, 45, 55))
