# 40. Write a Python program to check two given integers, each in the range 10..99, 
# return true if there is a digit that appears in both numbers.

def check_two(num1, num2):
    if num1 in range(10, 100) and num2 in range(10, 100):
        num1_digit = num1 % 10
        num2_digit = num2 % 10
        num1 = num1 // 10
        num2 = num2 // 10
        return num1 == num2 or num1 == num2_digit or num1_digit == num2 or num1_digit == num2_digit
    
print(check_two(19, 22))
print(check_two(15, 55))
print(check_two(99, 19))
