# 11. Write a Python program to create a new array with the elements in reverse order from a given an array of integers length 3.
def reverse(arr):
    return arr[::-1]


print("Reverse array")
print(reverse([1, 2, 5]))
print(reverse([7, 8, 9]))
print(reverse([3, 9, 10]))


# 12. Write a Python program to find the larger between the first and last elements of a given array of integers and length 3.
# Replace all the other values to be that value. Return the changed array.


def larger(arr):
    new_arr = [None, None, None]
    if arr[2] > arr[0]:
        new_arr[0], new_arr[1], new_arr[2] = arr[2], arr[2], arr[2]
    else:
        new_arr[0], new_arr[1], new_arr[2] = arr[0], arr[0], arr[0]

    return new_arr


print("\nMax value")
print(larger([1, 2, 5]))
print(larger([1, 2, 3]))
print(larger([7, 2, 4]))


# 13. Write a Python program to concatenate an array of arrays into one.
def array_of_arrays(nestedlist):
    flatlist = []
    for sublist in nestedlist:
        for element in sublist:
            flatlist.append(element)
    return flatlist


print("\nList of lists")
print(array_of_arrays([[1, 2, 3, 4], ["Ten", "Twenty",
      "Thirty"], [1.1,  1.0E1, 1+2j, 20.55, 3.142]]))


# 14. Write a Python program to check if a given array of integers contains 3 twice, or 5 twice.
def three_or_five(arr):
    threes = arr.count(3)
    fives = arr.count(5)
    return threes == 2 or fives == 2


print("\nThrees or fives in a list")
print(three_or_five([3, 5, 4, 6, 3, 3]))
print(three_or_five([5, 4, 5, 7, 2, 3]))


# 15. Write a Python program to find the largest odd value from a given array.
def max_odd(arr):
    max_val = 0
    for el in arr:
        if el % 2 != 0:
            if el > max_val:
                max_val = el
    return max_val


print("\nMax odd")
print(max_odd([1, 5, 4, 17, 22]))


# 16. Write a Python program to create a new array using the first three elements of a given array of integers.
def first_three(arr):
    new_arr = arr[:3]
    return new_arr


print("\nNew array givint first three integers")
print(first_three([1, 2, 3, 4, 5]))
print(first_three([1, 2]))
print(first_three([1]))


# 17. Write a Python program to get the number of even integers in a given array.
def even(arr):
    count = 0
    for element in arr:
        if element % 2 == 0:
            count += 1
    return count

print("\nEven elements in an array")
print(even([1, 2, 3, 4, 2, 5]))
print(even([1]))
print(even([1, 3, 6]))


# 18. Write a Python program to find the difference between the largest and smallest values of a given array of integers.
def difference(arr):
    max = 0
    min = arr[0]
    for element in arr:
        if(element > max):
                max = element
        elif(element < min):
                min = element
    return max - min


print("\nDifference max and min")
print(difference([1, 3, 4, 7]))
print(difference([1, 9]))
print(difference([19, 15, 34]))


# 19. Write a Python program to compute the average values of a given array of except the largest and smallest values.
def average(arr):
    max = 0
    min = arr[0]
    for element in arr:
        if(element > max):
            max = element
        elif(element < min):
            min = element 
    return (sum(arr) - max - min) / (len(arr) - 2)


print("\nAverage except min and max")
print(average([1, 3, 5, 7]))
print(average([10, 17, 2]))
print(average([12]))


# 20. Write a Python program to compute the sum of the numbers of a given array
# except for the number 17 and numbers that come immediately after a 17.
def sum_of_elements(array):
    sum = 0
    for element in array:
        if element == 17:
            break
        sum += element
    return sum


print("\nSum of elements excluding 17 and above")
print(sum_of_elements([3, 17])) 
print(sum_of_elements([10, 12, 21, 17, 34]))
print(sum_of_elements([9, 5, 18]))
