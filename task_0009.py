# 9. Write a Python program to check three numbers and return true if one or the other is small, but not both. A number is called "small" if it is in the range 1..10 inclusive. 
# Sample Output:
# true
# true
# false

def only_one_small(num1, num2):
    return (((num1 >= 1 and num1 <= 10) and not(num2 >= 1 and num2 <= 10)) or (not(num1 >= 1 and num1 <= 10) and (num2 >= 1 and num2 <= 10)))
    # (((a >= 1 && a <= 10) && !(b >= 1 && b <= 10)) || (!(a >= 1 && a <= 10) && (b >= 1 && b <= 10)));
    

print(only_one_small(2, 17))
print(only_one_small(20, 21))
print(only_one_small(15, 17))
print(only_one_small(10, 17))
