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

def fileRun(filename):
    ''' Read and parse through the file '''

    new_bst = BST()

    with open(filename, "r", encoding= "utf-8") as file:
        for line in file:
            file_read = parseLine(line)
            if file_read is None:
                continue 
            op_code, student = file_read
            if op_code == "I":
                new_bst.insert(student)
            elif op_code == "D":
                new_bst.delete(student.key)
    return new_bst

# Creating the node class
class Node:

    def __init__(self, student):
        self.data = student
        self.left = None
        self.right = None
        self.parent = None
    
# Binary Search Tree class
class BST:

    def __init__(self):
        self.root = None

    def insert(self, student):
        ''' Inserts/attach the node in the tree. it creates the node from student() and then
        assigns the node to the tree, then connects it'''
        new_node = Node(student)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if new_node.data.key < current.data.key:
                    if current.left is None:
                        current.left = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.right

    def search(self, key):
        ''' Search for nodes in the tree '''
        current = self.root
        
        while current is not None:
            if key == current.data.key:
                return current
            if key < current.data.key:
                current = current.left
            else:
                current = current.right
        return None
    
    def delete(self, key):
        ''' Delete a node in the tree '''
        node = self.search(key)

        if node is None:
            print(f"Warning {key} not found")
            return
        
        # delete a leaf
        if node.left is None and node.right is None:
            parent = node.parent
            if parent is None:
                self.root = None
            else:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None

        # delete a node w/ child 
        elif node.left is None or node.right is None:
            if node.left is not None:
                child = node.left
            else:
                child = node.right
            parent = node.parent

            if parent is None:
                root = child
            elif parent.left is node:
                parent.left = child
            else:
                parent.right = parent
            
            child.parent = parent

        # delete with two children
        else:
            successor = node.right
            while successor.left is not None:
                successor = successor.left

            node.data = successor.data

            # Removing the successor 
            child = successor.right
            parent = successor.parent

            if parent.left is successor:
                parent.left = child
            else:
                parent.right = child
            
            if child is not None:
                child.parent = parent


# Test
student_tree = fileRun("tree-input.txt")
print(student_tree.root.data)
zot = student_tree.search("zot")
doyle = student_tree.search("doyle")

if zot is None:
    print("Name was not found")
else:
    print(zot.data)

if doyle is None:
    print("Name was not found")
else:
    print(doyle.data)
print("-----------------------")

# TEST: Create a BST and add student to it 
tree = BST()
(op_code, mckay) = parseLine("I8534534McKay                    0251CT  1")
(op_code, black) = parseLine("I8499120Black                    0341RST 1")
(op_code, laporte) = parseLine("I8400342LaPorte                  0045JA  1")

# Testing the insert
tree.insert(mckay)
tree.insert(black)
tree.insert(laporte)

# Test the tree pathing
print(tree.root.data)
print(tree.root.left.data)
print(tree.root.left.right.data)
print(tree.root.left.right.parent.data)

# Testing search for in the tree and not in the tree
search_1 = tree.search("laporte")
search_2 = tree.search("zot")

if search_2 is None:
    print("Name was not found")
else:
    print(search_2.data)

if search_1 is None:
    print("Name was not found")
else:
    print(search_1.data)


# Testing deleting a leaf
#tree.delete("laporte")
#print(tree.root.left.right)

tree.delete("zot")
print(tree.root.right)


# Testing deleting a nod with one child
tree.delete("black")
print(tree.root.left.data)
print(tree.root.left.parent.data)

print("--------------")

# testing delete w/two children on a new tree
another_tree = BST()
(op_code, mckay) = parseLine("I8534534McKay                    0251CT  1")
(op_code, laporte) = parseLine("I8400342LaPorte                  0045JA  1")
(op_code, schafer) = parseLine("I8212399Schafer                  0251EST 1")
(op_code, morrison) = parseLine("I8322889Morrison                 0045JA  3")
(op_code, phillips) = parseLine("I8412094Phillips                 0251EST 1")

another_tree.insert(mckay)
another_tree.insert(laporte)
another_tree.insert(schafer)
another_tree.insert(phillips)
another_tree.insert(morrison)

another_tree.delete("mckay")
print(another_tree.root.data)
print(another_tree.root.right.left.data)
print(another_tree.root.right.left.left)

#student_1 = Student("8534534", "McKay", "0251", "CT", "1")
#node = Node(student_1)
#print(node.data, node.left, node.right, node.parent)





# Test to ensure that all 31 students print
#fileRun("tree-input.txt")


    

# Test to check that the function works
#(op, student) = parseLine("I8400342LaPorte                  0045JA  1")
#print(op)
#print(student)

# Faliure Test:
#parseLine("")
#parseLine("Z8400342LaPorte                  0045JA  1")
#parseLine("I8534534McKay                    0251CT  1")

#student_1 = Student("8534534", "McKay", "0251", "CT", "1")
#print(student_1)
#print(student_1.key)



    
       


