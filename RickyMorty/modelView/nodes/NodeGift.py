from modelView.Types import RickStacks
from modelView.nodes.NodeSimple import NodeSimple

class NodeGift(NodeSimple) :
    def __init__(self) :
        super().__init__()
        self.stack = None

    def getStack(self):
        return self.stack

    def setStack(self, stack):
        self.stack = stack
