class Node:
    def __init__(self):
        self.label = None
        self.children = {}
	    # you may want to add additional fields here...
        self.examples = []  # list of examples that are at this node
        self.isLeaf = 0
    def addChild(self, node, value):
        self.children[value] = node
    def addExamples(self, examples):
        self.examples = self.examples + examples
    def setLeaf (self):  # Setting the node as a leaf node
        self.isLeaf = 1
        self.children = {}
