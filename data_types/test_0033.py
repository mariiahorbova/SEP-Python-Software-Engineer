# 33. Write a Python program to check two positive integer values and return the larger value that is in the range 20..30 inclusive, 
# or return 0 if no number is in that range.
# Sample Output:
# 0
# 29
# 30
# 0

def return_larger(num1, num2):
    if (num1 >= 20 and num1 <= 30) and (num2 >= 20 and num2 <= 30):
        return max(num1, num2)
    else:
        return 0
    
    
print(return_larger(22, 30))
print(return_larger(17, 25))
print(return_larger(25, 23))
print(return_larger(19, 32))
