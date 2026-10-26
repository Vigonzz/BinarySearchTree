# File to run test from student.py
from student import *





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

order_tree = fileRun("tree-input.txt")
traverse_list  = order_tree.inOrderTraversal()

for node in traverse_list:
    print(node.data)

print(len(traverse_list))
