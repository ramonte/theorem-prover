from node import Node
import argparse
import basic
import improved
import copy
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Analytic tableaux')
    parser.add_argument('-i', help='use improved version', action='store_true')

    ''' required arguments '''
    required = parser.add_argument_group('required arguments')
    required.add_argument('-f', help='path to file', required=True)

    args = parser.parse_args()
    formulas = read_formulas(args.f)
    if (args.i):
        value, branches, rules = improved.start(formulas)
    else:
        value, branches, rules = basic.start(formulas)
    if (value == True):
        print ('\ntrue!')
    else:
        print ('\nfalse for:', value)
    print ('branches:', branches, '| nodes:', rules)

def create_tree(prop):
    if (prop):
        if (len(prop) == 0):
            return None, None
        if (prop[0] == ' '):
            prop = prop[1:]
    else:
        return None, None
    token = prop[0]
    if (token.isdigit()):
        size = 1
        if (len(prop) > 1):
            if (prop[1].isdigit()):
                token += prop[1]
                size = 2
        node = Node(token)
        node.left = None
        node.right = None
        return node, prop[size:]
    else:
        node = Node(token)
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

    if (1 + int(lines[0]) != len(lines)):
        last, _ = create_tree(lines[len(lines)-1])
        last.valuation = False
        formulas.append(last)
    return formulas

if __name__ == '__main__':
    main()
