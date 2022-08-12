# 7. Write a Python program to accept a filename from the user to print the extension of that. (With Regexp)
# Sample Output:
# Filename: test.rb
# Base name: test
# Extension: .rb
# Pathname: / user/system

import re


def split_filename():
    filename = input("Input a filename:")
    splited = re.split('\W+', filename)
    # print(splited)
    print("Filename:", ".".join(splited[-2:]))
    print("Basename:", "".join(splited[-2:-1]))
    print("Extention:", "." + "".join(splited[-1:]))
    print("Pathname:", "/".join(splited[:-2]))


split_filename()
