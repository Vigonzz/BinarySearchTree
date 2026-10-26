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


def parseLine(raw_line):
    ''' The function will take in a raw line of text from the file and then turns it into
    an object that may be utilized by opcode and a Student object'''

    raw_line = raw_line.rstrip()
    if len(raw_line) < 42:
        print(f"line is too short, '{raw_line}'")
        return None
    
    op_code = raw_line[0:1]
    student_number = raw_line[1:8]
    last_name = raw_line[8:33]
    department = raw_line[33:37]
    program = raw_line[37:41]
    year = raw_line[41:42]

    # Check OP-code to pass valid characters
    if op_code not in ("I", "D"):
        print(f"Not valid: {op_code}")
        return None
    
    # Cleaning the fields
    last_name = last_name.strip() 
    department = department.strip()
    program = program.strip()
    year = year.strip()

    student_2 = Student(student_number, last_name, department, program, year)
    return (op_code, student_2)
    
(op, student) = parseLine("I8400342LaPorte                  0045JA  1")
print(op)
print(student)

# Faliure Test:
parseLine("")
parseLine("Z8400342LaPorte                  0045JA  1")
parseLine("I8534534McKay                    0251CT  1")

student_1 = Student("8534534", "McKay", "0251", "CT", "1")
print(student_1)
print(student_1.key)



    
       


