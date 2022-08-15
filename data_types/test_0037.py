# 37. Write a Python program to check two given integers and return 11 if either one is 11. 
# Return their sum or difference if sum or difference is 11.

def check_11(num1, num2):
    return num1 == 11 or num2 == 11 or num1 + num2 == 11 or abs(num1 - num2) == 11


print(check_11(11, 25))
print(check_11(10, 50))
print(check_11(52, 41))
print(check_11(5, 16))
