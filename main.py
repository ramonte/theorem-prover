from node import Node
import copy
import numpy as np

def main():
    # string = ')+12*-13'
    string = ')*-)12+3-23'
    tree, st = create_tree(string)
    print (str(tree))

def create_tree(prop):
    print (prop)
    if (prop):
        if (len(prop) == 0):
            return None, None
    else:
        return None, None
    token = prop[0]
    node = Node(token)
    if (token.isdigit()):
        node.left = None
        node.right = None
        return node, prop[1:]
    else:
        if (token != '-'):
            node.left, st = create_tree(prop[1:])
            node.right, st = create_tree(st)
        else:
            node.right, st = create_tree(prop[1:])
    return node, st


if __name__ == '__main__':
    main()
