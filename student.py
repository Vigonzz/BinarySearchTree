# Violet Gonzalez, Oct 25, 2026

# Task 1:
# Build a Binary Search Tree (BST) using the data from the input fileDownload input file. 
# Both insertion into and deletion from the tree will be done. The tree should be ordered by 
# the student's last name (use a case-insensitive comparison). There are only unique records 
# in the input file. Each node must contain the student data (exclude the operation code), a 
# left child pointer, and a right child pointer. A parent pointer is optional but might prove 
# helpful in some operations.

class Student:

    def __init__(self, student_number, last_name, department, program, year):
        self.student_number = student_number
        self.last_name = last_name
        self.department = department
        self.program = program
        self.year = year
        self.key = self.last_name.lower()

    def __str__(self):
       ''' Method for returning a student ad a line of text to the output file '''
       return f"Student Id:{self.student_number}, L Name:{self.last_name}, Department:{self.department}, Program:{self.program}, Year:{self.year}"

student_1 = Student("8534534", "McKay", "0251", "CT", "1")
print(student_1)
print(student_1.key)



    
       


