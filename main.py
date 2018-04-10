from node import Node
import copy
import numpy as np

def main():
    string = ')+12*-13'
    tree, st = create_tree(string)
    print (str(tree))

def create_tree(prop):
    print (prop)
    if (len(prop) == 0):
        return None, None
    token = prop[0]
    node = Node(token)
    if (token.isdigit()):
        node.left = None
        node.right = None
        return node, prop[1:]
    else:
        print ('e')
        node.left, st = create_tree(prop[1:])
        print ('d')
        node.right, st = create_tree(st)
    return node, st


if __name__ == '__main__':
    main()
