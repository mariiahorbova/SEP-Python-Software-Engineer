# 26. Write a Python program to retrieve the total marks where subject name and marks of a student stored in a hash.
# Sample subject and marks: Literature - 74, Science – 89, Math-91
# Sample Output:
# Total Marks: 254


def hash_marks():
    st_marks = {}
    summary = 0
    st_marks["Literature"] = 74
    st_marks["Science"] = 89
    st_marks["Math"] = 91
    for mark in st_marks.values():
        summary += mark
    return summary

print(hash_marks())
