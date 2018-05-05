from node import Node
import argparse
import copy
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Tableaux')

    ''' required arguments '''
    required = parser.add_argument_group('required arguments')
    required.add_argument('-f', help='path to file', required=True)

    args = parser.parse_args()
    formulas = read_formulas(args.f)

    for f in formulas:
        print (f)
    # string = ')+12*-13'
    # string = ')*-)12+3-23'
    # tree, st = create_tree(string)
    # print (str(tree))

def create_tree(prop):
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

def read_formulas(filename):
    lines = [line.rstrip('\n') for line in open(filename)]

    if not (lines[0].isdigit()):
        raise Exception('The first argument in the file must be a number')

    formulas = []
    for i in range(1, 1 + int(lines[0])):
        node, _ = create_tree(lines[i])
        node.valuation = True
        formulas.append(node)

    last, _ = create_tree(lines[len(lines)-1])
    last.valuation = False
    formulas.append(last)
    return formulas

if __name__ == '__main__':
    main()
