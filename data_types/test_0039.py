# 39. Write a Python program to check two given integers and return the larger value. 
# However, if the two values have the same remainder when divided by 5 then return the smaller value 
# and if the two values are the same, return 0.
# Sample Output:
# 12
# 110
# 0

def check_two(num1, num2):
    if num1 == num2:
        return 0
    if num1 % 5 == num2 % 5:
        return min(num1, num2)
    return max(num1, num2)


print(check_two(20, 50))
print(check_two(5, 7))
print(check_two(84, 84))
