# 2. Write Python program to display the current date and time.

# Sample Output:
#       Current Date and Time: 27/12/2017 06: 04

import datetime

time_now = datetime.datetime.now()

print(time_now.strftime("Current Date and Time: %d/%m/%Y %H:%S"))
