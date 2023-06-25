from Node import Node
import copy
class AVLTree:
    def __init__(self) -> None:
        self.HeadNode = None
    
    def RecursiveInsert(self,ValueToInsert:int,Subtree=None):
        if self.HeadNode == None:
                self.HeadNode = Node(ValueToInsert)
                self.HeadNode.Height = 1 + max(self.GetHeight(self.HeadNode.LeftNode),self.GetHeight(self.HeadNode.RightNode))
                self.HeadNode.BalanceFactor = self.GetBalance(Subtree)
                self.printTree(self.HeadNode)
                print("\n")
        else:
            if Subtree == None:
                Subtree = self.HeadNode
            if ValueToInsert > Subtree.Value and Subtree.RightNode != None:
                self.RecursiveInsert(ValueToInsert,Subtree.RightNode)
            elif ValueToInsert <= Subtree.Value and Subtree.LeftNode != None:
                self.RecursiveInsert(ValueToInsert,Subtree.LeftNode)
            if ValueToInsert > Subtree.Value and Subtree.RightNode == None:
                Subtree.RightNode = Node(ValueToInsert)
            elif ValueToInsert <= Subtree.Value and Subtree.LeftNode == None:
                Subtree.LeftNode = Node(ValueToInsert)
            
            # self.printTree(Subtree)

            # print("\n")

            self.printTree(self.HeadNode)

            print("\n")
            
            Subtree.Height = 1 + max(self.GetHeight(Subtree.LeftNode),self.GetHeight(Subtree.RightNode))

            Subtree.BalanceFactor = self.GetBalance(Subtree)

            #Left Left
            # if Subtree.BalanceFactor > 1 and ValueToInsert < Subtree.LeftNode.Value:
            #     self.RightRotate(Subtree)
            # #Left Right
            # elif Subtree.BalanceFactor > 1 and ValueToInsert > Subtree.LeftNode.Value:
            #     LeftNode = Subtree.LeftNode
            #     self.LeftRotate(LeftNode)
            #     self.RightRotate(Subtree)
            # #Right Right
            # elif Subtree.BalanceFactor < 1 and ValueToInsert > Subtree.RightNode.Value:
            #     self.LeftRotate(Subtree)
            # #Right Left
            # elif Subtree.BalanceFactor < 1 and ValueToInsert < Subtree.RightNode.Value:
            #     RightNode = Subtree.RightNode
            #     self.RightRotate(RightNode)
            #     self.LeftRotate(Subtree)

            #If Subtree.BalanceFactor -ve, right skewed
            #If Subtree.BalanceFactor +ve, left skewed

            #Imbalance in the left child's right subtree
            if Subtree.BalanceFactor > 1 and self.GetHeight(self.GetLeftChild(Subtree.LeftNode)) <= self.GetHeight(self.GetRightChild(Subtree.LeftNode)):
                LeftNode = Subtree.LeftNode
                self.LeftRotate(LeftNode)
                self.RightRotate(Subtree)
            #Imbalance in the left child's left subtree
            elif Subtree.BalanceFactor > 1 and self.GetHeight(self.GetLeftChild(Subtree.LeftNode)) > self.GetHeight(self.GetRightChild(Subtree.LeftNode)):
                self.RightRotate(Subtree)
            #Imbalance in the right child's left subtree
            elif Subtree.BalanceFactor < -1 and self.GetHeight(self.GetLeftChild(Subtree.RightNode)) > self.GetHeight(self.GetRightChild(Subtree.RightNode)):
                RightNode = Subtree.RightNode
                self.RightRotate(RightNode)
                self.LeftRotate(Subtree)
            #Imbalance in the right child's right subtree
            elif Subtree.BalanceFactor < -1 and self.GetHeight(self.GetLeftChild(Subtree.RightNode)) < self.GetHeight(self.GetRightChild(Subtree.RightNode)):
                self.LeftRotate(Subtree)
            # print(self.HeadNode)

            # print("\n")

            self.printTree(self.HeadNode)

            print("\n")
        # if Subtree == None:
        #     Subtree = self.HeadNode
        # if self.HeadNode == None:
        #     self.HeadNode = Node(ValueToInsert)
        # elif ValueToInsert > Subtree.Value and Subtree.RightNode != None:
        #     self.RecursiveInsert(ValueToInsert,Subtree.RightNode)
        # elif ValueToInsert <= Subtree.Value and Subtree.LeftNode != None:
        #     self.RecursiveInsert(ValueToInsert,Subtree.LeftNode)
        # if ValueToInsert > Subtree.Value and Subtree.RightNode == None:
        #     Subtree.RightNode = Node(ValueToInsert)
        # elif ValueToInsert <= Subtree.Value and Subtree.LeftNode == None:
        #     Subtree.LeftNode = Node(ValueToInsert)
        

        # if self.HeadNode == None:
        #     self.HeadNode = Node(ValueToInsert)
        # else:
        #     if Subtree == None:
        #         Subtree = self.HeadNode
        #     elif ValueToInsert > Subtree.Value and Subtree.RightNode != None:
        #         self.RecursiveInsert(ValueToInsert,Subtree.RightNode)
        #     elif ValueToInsert <= Subtree.Value and Subtree.LeftNode != None:
        #         self.RecursiveInsert(ValueToInsert,Subtree.LeftNode)
        #     if ValueToInsert > Subtree.Value and Subtree.RightNode == None:
        #         Subtree.RightNode = Node(ValueToInsert)
        #     elif ValueToInsert <= Subtree.Value and Subtree.LeftNode == None:
        #         Subtree.LeftNode = Node(ValueToInsert)

    def printTree(self,node:Node, level=0):
        if node != None:
            self.printTree(node.LeftNode, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.Value) + f",{node.Height},{node.BalanceFactor}")
            self.printTree(node.RightNode, level + 1)
    
    def GetLeftChild(self,Node:Node):
        if Node == None:
            return None
        else:
            return Node.LeftNode
    
    def GetRightChild(self,Node:Node):
        if Node == None:
            return None
        else:
            return Node.RightNode


    def LeftRotate(self,Subtree: Node):
        print(f"L at {Subtree.Value} \n")
        Copy = copy.deepcopy(Subtree)
        RightNode = Copy.RightNode
        Copy.RightNode = RightNode.LeftNode
        RightNode.LeftNode = Copy
        Subtree.LeftNode = RightNode.LeftNode
        Subtree.RightNode = RightNode.RightNode
        Subtree.Value = RightNode.Value
        Subtree.Height = RightNode.Height


        # Subtree.Height = 1 + max(self.GetHeight(Subtree.LeftNode),self.GetHeight(Subtree.RightNode))
        # RightNode.Height = 1 + max(self.GetHeight(RightNode.LeftNode),self.GetHeight(RightNode.RightNode))

        Subtree.LeftNode.Height = 1 + max(self.GetHeight(Subtree.LeftNode.LeftNode),self.GetHeight(Subtree.LeftNode.RightNode))
        Subtree.Height = 1 + max(self.GetHeight(Subtree.LeftNode),self.GetHeight(Subtree.RightNode))


    def RightRotate(self,Subtree: Node):
        print(f"R at {Subtree.Value} \n")
        Copy = copy.deepcopy(Subtree)
        LeftNode = Copy.LeftNode
        Copy.LeftNode = LeftNode.RightNode
        LeftNode.RightNode = Copy
        Subtree.LeftNode = LeftNode.LeftNode
        Subtree.RightNode = LeftNode.RightNode
        Subtree.Value = LeftNode.Value
        Subtree.Height = LeftNode.Height

        Subtree.RightNode.Height = 1 + max(self.GetHeight(Subtree.RightNode.LeftNode),self.GetHeight(Subtree.RightNode.RightNode))
        Subtree.Height = 1 + max(self.GetHeight(Subtree.LeftNode),self.GetHeight(Subtree.RightNode))

    #To handle null values
    def GetHeight(self,Node:Node):
        if Node == None:
            return 0
        return Node.Height

    def GetBalance(self,Node:Node):
        if Node == None:
            return 0
        return self.GetHeight(Node.LeftNode) - self.GetHeight(Node.RightNode)

    def InOrderTraversal(self,node: Node):
        if node.LeftNode != None:
        #    print("L")
            self.InOrderTraversal(node.LeftNode)
        #print("E")
        print(node.Value)
        if node.RightNode != None:
        #    print("R")
            self.InOrderTraversal(node.RightNode)

    def PreOrderTraversal(self,node: Node):
        print(node.Value)
        if node.LeftNode != None:
        #    print("L")
            self.InOrderTraversal(node.LeftNode)
        if node.RightNode != None:
        #    print("R")
            self.InOrderTraversal(node.RightNode)