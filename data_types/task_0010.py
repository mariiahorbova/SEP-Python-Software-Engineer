# 10. Write a Python program to print the following 'here document'. 
# Sample string: a string that you "don't" have to escape This is a ....... multi-lineheredoc string - ------ -> example
# Sample Output:

# Sample string:
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string - ------ -> example

sample_string = """Sample string :
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""

print(sample_string)

# if user enters something like "don't" or \n it will be shown as ordinary text
sample_string_input = input("Input a string: ")
print(sample_string_input)
