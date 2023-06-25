class Node:
    def __init__(self,Value,LeftNode=None,RightNode=None) -> None:
        self.Value = Value
        self.BalanceFactor = 0
        self.Height = 1
        self.LeftNode = LeftNode
        self.RightNode = RightNode