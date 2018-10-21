class Tree():
    def __init__(self, root,val, children = []):
        self.root = root
        self.val = val
        #each child is in the list
        self.children = children
        #Sum of all of nodes's values
        self.sum = 0

    def getVal(self):
        return self.val

    def getSum(self):
        return self.sum

    def getChildren(self):
        return self.children

    def deepSearch(self):
        pass

    def printTree(self):
        pass


a = Tree("r", 2, [Tree("a", -5,[Tree("c", 4),Tree("d",-1),Tree("e", -1)]),Tree("b",-1, [Tree("f", -1), Tree("g", -2), Tree("h",2)])])
