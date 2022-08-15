# 16. Write a Python program to find the greatest of three numbers. 
# Sample Output:
# y = 5 is greatest.

def greater(a, b, c):
    if a > b and a > c:
        return f"a = {a} is the greatest"
    elif b > a and b > c:
        return f"b = {b} is the greatest"
    else:
        return f"c = {c} is the greatest"
    
print(greater(2, 3, 4))
print(greater(7, 2, 5))
print(greater(4, 90, 13))
