#!/usr/bin/python
from bst_pygraphviz import *

class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

def bst_print_iterative(root):
    """ print in terminal """
    tmp_A = []
    while len(tmp_A) > 0 or root != None:
        if root != None:
            tmp_A.append(root)
            root = root.left
        else:
            root = tmp_A.pop()
            print root.num
            root = root.right

def _bst_depth(root, size):
    """ Find the bst depth, recursive """
    if root == None:
        return size
    size += 1
    l = _bst_depth(root.left, size)
    r = _bst_depth(root.right, size)
    return max(l, r)

def bst_depth_iterative(root):
    """ Find the bst depth """
    depth = 0
    wq = [root]
    path = []
    while ( len(wq) > 0 ):
        r = wq[-1]
        if ( len(path) > 0 and r == path[-1]):
            if (len(path) > depth):
                depth = len(path)
            path.pop()
            wq.pop()
        else:
            path.append(r)
            if (r.right != None):
                wq.append(r.right)
            if (r.left != None):
                wq.append(r.left)
    return depth

def bst_insert(root, n):
    if root == None:
        return n
    if n.num < root.num:
        root.left = bst_insert(root.left, n)
    else:
        root.right = bst_insert(root.right, n)
    return root

def bst_insert_numbers(numbers):
    if len(numbers) < 1: return None
    root = Node(numbers[0])
    for n in numbers[1:]:
        bst_insert(root, Node(n))
    return root

def pre_order_list(root, pre_list):
    if root == None:
        return
    pre_list.append(root.num)
    pre_order_list(root.left, pre_list)
    pre_order_list(root.right, pre_list)


def diff(a, b):
    diff = a-b
    if diff < 0:
        diff *= -1
    return diff

def avl_balanced(root):
    """ Check if bst is AVL balanced """
    if root == None:
        return True
    # Checking max depth of root.left, root.right
    l = _bst_depth(root.left, 0)
    r = _bst_depth(root.right, 0)
    df = diff(l,r)
    if df > 1:
        return False
    l_val = avl_balanced(root.left)
    r_val = avl_balanced(root.right)
    if l_val==False or r_val == False:
        return False
    return True

def perfect_balanced(root):
    """ Simple test.
    check if bst is perfect balanced """
    if root == None:
        return True
    l = _bst_depth(root.left, 0)
    r = _bst_depth(root.right, 0)
    df = diff(l,r)
    if df >= 1:
        return False
    l_val = perfect_balanced(root.left)
    r_val = perfect_balanced(root.right)
    if l_val==False or r_val==False:
        return False
    return True

def in_order_list(root, A):
    # RETURN NODE
    if root == None:
        return
    in_order_list(root.left, A)
    A.append(root)
    in_order_list(root.right, A)

def nodes_to_sorted_bst(A, start, end):
    mid = (start+end)/2
    if start > end:
        return None
    n = A[mid]
    n.left = nodes_to_sorted_bst(A,start,mid-1)
    n.right = nodes_to_sorted_bst(A,mid+1, end)
    return n

def example():

    numbers = [ 55, -44, 666, -1337, 0,-1,-2,2,1,3,-1, 66, 67, 68, 69]

    root = bst_insert_numbers(numbers)

    # balanced bst
    inorder = []
    in_order_list(root, inorder)
    root = nodes_to_sorted_bst(inorder, 0, len(inorder)-1)

    print "depth is ", _bst_depth(root, 0)
    print "AVL balanced:", avl_balanced(root)
    print "perfect balanced:", perfect_balanced(root)

    # Draw bst to png, tree.png
    pre_list = []
    pre_order_list(root, pre_list)

    create_tree(pre_list)

if __name__ == "__main__":
    example()

