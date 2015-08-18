import pygraphviz as pgv
import random

class Node_graphing:
    insertion_step = []

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addNode_graphing(self, data):
        if data < self.data:
            if self.left == None:
                self.left = Node_graphing(data)
                self.printSubtree()
            else:
                # recursively calling method
                self.left.addNode_graphing(data)  
        else:
            if self.right == None:
                self.right = Node_graphing(data)
                self.printSubtree()
            else:
                self.right.addNode_graphing(data)

    def printSubtree(self):
        if not (self.left == None or self.right == None):
            self.insertion_step.append((self.left.data, self.data, self.right.data))
        elif (self.left == None and not self.right == None):
            self.insertion_step.append((None, self.data, self.right.data))
        elif (not self.left == None and self.right == None):
            self.insertion_step.append((self.left.data, self.data, None))
        else:
            self.insertion_step.append((None, self.data, None))

    def drawTree(self, tree, f):
        id = 0
        # queue nodes
        nodes = [(None, self)]  

        while nodes:
            parent, node = nodes.pop(0)
            tree.add_node(id, label=node.data, color='goldenrod2', style='filled')

            if parent != None:
                weight = 1
                if tree.get_node(parent).attr['label'] == str(node.data):
                    # same value, increase weight of edge to straighten it.
                    weight = 10
                tree.add_edge(parent, id, color='sienna', style='filled', weight=weight)

            if node.left != None:
                nodes.append((id, node.left))
            else:
                none_id = '{}_left_none'.format(id)
                tree.add_node(none_id, label='', color='goldenrod1', shape='box', style='filled')
                tree.add_edge(id, none_id, color='sienna', style='filled')

            if node.right != None:
                nodes.append((id, node.right))
            else:
                none_id = '{}_right_none'.format(id)
                tree.add_node(none_id, label='', color='goldenrod1', shape='box', style='filled')
                tree.add_edge(id, none_id, color='sienna', style='filled')

            id += 1

        tree.write(f)
        img = pgv.AGraph(f)
        img.layout(prog='dot')
        img.draw(f.split('.')[0] + '.png')
        img.close()


def create_tree(lst):

    n = Node_graphing(lst[0])

    n.printSubtree()
    for num in lst[1:]:
        n.addNode_graphing(num)

    tree = pgv.AGraph(directed=True, strict=True)
    filename = 'tree.dot'
    n.drawTree(tree, filename)

