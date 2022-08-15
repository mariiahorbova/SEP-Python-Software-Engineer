# 28. Write a Python program to test whether a year is leap year or not.
# Sample Output:
# 2012 is leap year
# 1500 is not leap year
# 1600 is leap year
# 2020 is leap year

def leap_year(year):
    if year % 400 == 0:
        return f"{year} is a leap year"
    elif year % 4 == 0 and year % 100 != 0:
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"


print(leap_year(2000))
print(leap_year(2120))
print(leap_year(2003))
print(leap_year(2012))
print(leap_year(1603))
