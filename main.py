from SelfBalancingTree import AVLTree
from Node import Node
import random

Tree = AVLTree()

for i in range(10):
    j = random.randint(50,100)
    Tree.RecursiveInsert(j)

# Tree.RecursiveInsert(10)
# Tree.RecursiveInsert(9)
# Tree.RecursiveInsert(8)
# Tree.RecursiveInsert(7)
# Tree.RecursiveInsert(6)
# Tree.RecursiveInsert(5)
# Tree.RecursiveInsert(4)
# Tree.RecursiveInsert(3)
# Tree.RecursiveInsert(2)
# Tree.RecursiveInsert(1)

def printTree(node:Node, level=0):
    if node != None:
        printTree(node.LeftNode, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.Value))
        printTree(node.RightNode, level + 1)

printTree(Tree.HeadNode)

print(Tree.HeadNode)