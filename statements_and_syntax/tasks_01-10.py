# 1. Write a Python program to check if a value exists in an array.
# Sample Output:
# Original array:
# ["Red", "Green", "Blue", "White"]
# Check if 'Green' in color array!
# true
# Check if 'Pink' in color array!
# false

from random import sample


def check_value_in_array(value):
    arr = ["Red", "Green", "Blue", "White"]
    print(f"Check if '{value}' in color array!")

    return True if value in arr else False


print(check_value_in_array('Green'))
print(check_value_in_array('Pink'))
print(check_value_in_array('Black'))
print(check_value_in_array('White'))


# 2. Write a Python program to check whether 7 appears as either the first or last element in a given array. The array length must be 1 or more.
# Sample Output:
# true
# true
# false

def check_seven(nums):
    return True if nums[0] == 7 or nums[len(nums)-1] == 7 else False


print("\nCheck seven")
print(check_seven([7, 4, 3, 6, 8]))
print(check_seven([3, 7, 5, 3]))
print(check_seven([1]))
print(check_seven([1, 5, 7]))


# 3. Write a Python program to pick a number of random elements from a given array.
# Sample Output:
# Original array:
# [12, 34, 23, 56]
# 2 random elements from the array.
# [34, 12]
# 3 random elements from the array.
# [56, 12, 34]


def random_sample(arr, n):
    return sample(arr, n)


print("\nRandom sample from a list")
print(random_sample([3, 4, 6, 8, 9, 13, 24, 67, 0], 5))


# 4. Write a Python program to check whether first and the last element are the same as a given array of integers. The array length must be 1 or more.
# Sample Output:
# false
# true
# false

def check_first_last(arr):
    return True if arr[0] == arr[len(arr)-1] else False


print("\nCheck equality")
print(check_first_last([1]))
print(check_first_last([7, 3, 9]))
print(check_first_last([0, 5, 1, 8, 0]))


# 5. Write a Python program to compute the sum of elements in a given array.
# Sample Output:
# Original array:
# [12, 34, 23, 56]
# Sum of the values of the above array:
# 125

def sum_of_array(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum


print("\nSum of elements in a given array")
print(sum_of_array([12, 34, 23, 56]))
print(sum_of_array([1, 3, 5, 7, 8, 9]))
print(sum_of_array([6, 8]))


# 6. Write a Python program to remove duplicate elements from a given array.
# Sample Output:
# Original array:
# [1, 2, 3, 4, 1, 2, 2, 3, 5, 6]
# Array with unique elements:
# [1, 2, 3, 4, 5, 6]

def remove_duplicate(nums):
    nums_unique = []
    for num in nums:
        if num not in nums_unique:
            nums_unique.append(num)
    return nums_unique


print("\nUnique elements in array")
print(remove_duplicate([1, 2, 3, 4, 1, 2, 2, 3, 5, 6]))
print(remove_duplicate([1, 2, 1, 8, 1, 6, 8, 9]))


# 7. Write a Python program to check two given arrays of integers and test if they have the same first element or they have the same last element.
# Both arrays length must be 1 or more.
# Sample Output:
# true
# false
# true

def check_two_arrays(nums, nums1):
    return (nums[0] == nums1[0] or nums[len(nums)-1] == nums1[len(nums1)-1])


print("\nCheck two arrays")
print(check_two_arrays([1, 2, 5], [7, 5]))
print(check_two_arrays([1, 2, 3], [7, 3, 2]))
print(check_two_arrays([1, 2, 4], [1, 4]))


# 8. Write a Python program to remove blank elements from a given array.
# Sample Output:
# Original array:
# ["Red", "Green", "", "Blue", "White"]
# Remove a blank element from the above array:
# ["Red", "Green", "Blue", "White"]

def remove_blank(arr):
    return [elem for elem in arr if elem]


print("\nRemove blank")
print(remove_blank(["Red", "Green", "", "Blue", "White"]))
print(remove_blank(["Red", "", "", "Blue", "White"]))


# 9. Write a Python program to split a delimited string into an array.
# Sample Output:
# Original delimited string:
# Red, Green, Blue, White1, 3, 4, 5, 7String to array:
# ["Red", " Green", " Blue", " White"]
# [1, 3, 4, 5, 7]

def split_delimited():
    colors = "Red, Green, Blue, White"
    nums = "1, 3, 4, 5, 7"
    s_colors = colors.split()
    s_nums = nums.split(",")
    s_int_nums = [int(x) for x in s_nums]
    return s_colors, s_int_nums


print("\nSplit string into array")
print(split_delimited())


# 10. Write a Python program to create an array with the elements "rotated left" of a given array of ints length 3.
# Sample Output:
# [2, 5, 1]
# [2, 3, 1]
# [2, 4, 1]

def rotated_left(nums):
    return nums[1], nums[2], nums[0]


print("\nRotate left")
print(rotated_left([1, 2, 5]))
print(rotated_left([2, 1, 3]))
print(rotated_left([1, 2, 4]))
