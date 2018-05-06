from node import Node
import argparse
import basic
import improved
import copy
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Analytic tableaux')

    ''' required arguments '''
    required = parser.add_argument_group('required arguments')
    required.add_argument('-f', help='path to file', required=True)
    required.add_argument('-i', help='use improved', action='store_true')

    args = parser.parse_args()
    formulas = read_formulas(args.f)
    if (args.improved):
        b, branches = improved.compute(formulas)
    else:
        b, branches = basic.compute(formulas)
    if (b == True):
        print ('\ntrue')
    else:
        print ('\nfalse for:', b)
    print ('branches: ', branches)

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
    lines = [line.rstrip('\n').replace(' ', '') for line in open(filename)]

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
