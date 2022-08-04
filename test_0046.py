# 46. Написати програму, яка із введеного користувачем цілого чотирьохзначного числа(наприклад 5141):
# знаходить суму цифр цього числа(5141 це 5+1+4+1=11).
# перевіряє чи є однакові цифри(двічі зустрічається цифра 1)
# перевіряє чи сума двох перших цифр чотирьохзначного числа рівна двом наступним
# (5141 → 5+1=6 і 4+1=5 → суми першої та другої пар цифр даного числа різні)

def four_digit_number():
    n = int(input("Input a four-digit number:"))
    d4 = n % 10
    d3 = n % 100 // 10
    d2 = n % 1000 // 100
    d1 = n // 1000
    sum = d1 + d2 + d3 + d4
    print("The sum of digits is", sum)
    if d1 == (d2 or d3 or d4) or d2 == (d3 or d4) or d3 == d4:
        print("There are two same digits in a number")
    else:
        print("There is no same digits in a number")
    
    if d1 + d2 == d3 + d4:
        print("The sum of two first digits is the same as the sum of last two")
    else:
        print("The sum of two first digits is not the same as the sum of last two")
    

four_digit_number()
