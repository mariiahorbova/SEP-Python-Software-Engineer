# 32. Write a Python program to check two integer values and return true if they are both in the range 10..20 inclusive, 
# or they are both in the range 20..30 inclusive.
# Sample Output:
# true
# false
# true
# false

def both_in_range(num1, num2):
    if ((num1 >= 10 and num1 <= 20) and (num2 >= 10 and num2 <= 20)) or ((num1 >= 20 and num1 <= 30) and (num2 >= 20 and num2 <= 30)):
        return True
    else:
        return False
    
print(both_in_range(22, 30))
print(both_in_range(1, 3))
print(both_in_range(12, 5))
print(both_in_range(27, 25))
