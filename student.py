# Violet Gonzalez, Oct 25, 2026

# Task 1:
# Build a Binary Search Tree (BST) using the data from the input fileDownload input file. 
# Both insertion into and deletion from the tree will be done. The tree should be ordered by 
# the student's last name (use a case-insensitive comparison). There are only unique records 
# in the input file. Each node must contain the student data (exclude the operation code), a 
# left child pointer, and a right child pointer. A parent pointer is optional but might prove 
# helpful in some operations.

# Structural guidance, some debugging, and step explanations were assisted with Claude Chat.
# ALL code is my own. https://claude.ai/share/12f36365-f37e-428b-b7bb-b94c2c4dde81

# Ramos, L. P. (2026, July 18). Python’s deque: Implement efficient queues and stacks. Real Python.
# https://realpython.com/python-deque/ 
from collections import deque


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
    
    def inOrderTraversal(self):
        traverse = []
        self.inOrderHelper(self.root, traverse)
        return traverse
    
    def inOrderHelper(self, node, traverse):
        if node is None:
            return
        self.inOrderHelper(node.left, traverse) 
        traverse.append(node)
        self.inOrderHelper(node.right, traverse)

    # From the skeleton provided in the assignments note
    # PreOrder
    def preOrder(self):
        traverse = []
        self.preOrder(self.root, traverse)
        return traverse
    
    def preOrderHelper(self, node, traverse):
        if node is None:
            return
        traverse.append(node)
        self.preOrderHelper(node.left, traverse) 
        self.preOrderHelper(node.right, traverse)

    #postOrder
    def postOrder(self):
        traverse = []
        self.postOrder(self.root, traverse)
        return traverse
    
    def postOrderHelper(self, node, traverse):
        if node is None:
            return
        self.postOrderHelper(node.left, traverse) 
        self.postOrderHelper(node.right, traverse)
        traverse.append(node)

    # I am using dequeue from pythons standard library as the queue
    def levelOrderTraversal(self):
        result_list = []
        if self.root is None:
            return result_list
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            result_list.append(node)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)
        return result_list

# Since I was using this with and for loop multiple times I just decided to go for 
# a function to clean up the file.. just a bit
def fileWrite(new_file, file_list):
    # Need to look at a reference to use w:
    # GeeksforGeeks. (2026a, April 4). Writing to file in Python. https://www.geeksforgeeks.org/python/writing-to-file-in-python/ 
    with open(new_file, "w", encoding="utf-8") as output_file:
        for node in file_list:
            output_file.write(str(node.data) + "\n")

                


if __name__ == "__main__":

    # Build the tree
    order_tree = fileRun("tree-input.txt")

    # Get the in-order list and level order list
    order_list  = order_tree.inOrderTraversal()
    level_list = order_tree.levelOrderTraversal()

    # Write the file
    fileWrite("inorder-output.txt", order_list)
    fileWrite("levelorder-output.txt", level_list)