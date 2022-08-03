# 24. Write a Python program to print the elements of a given array. 
# Sample array: ["Ruby", 2.3, Time.now]
from datetime import datetime

def print_elements():
    sample = ["Ruby", 2.3, datetime.now().strftime("%H:%M:%S")]
    for el in sample:
        print(el)
        
print_elements()
