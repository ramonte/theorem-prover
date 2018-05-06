from copy import deepcopy

'''
Alpha:
    T ~A   : FA
    F ~A   : TA
    TA ^ B : TA/TB
    FA v B : FA/FB
    FA -> B: TA/FB
'''
def t_neg(node):
    child = deepcopy(node.right)
    child.valuation = False
    return (child, None)

def f_neg(node):
    child = deepcopy(node.right)
    child.valuation = True
    return (child, None)

def t_and(node):
    childl = deepcopy(node.left)
    childr = deepcopy(node.right)
    childl.valuation = True
    childr.valuation = True
    return (childl, childr)

def f_or(node):
    childl = deepcopy(node.left)
    childr = deepcopy(node.right)
    childl.valuation = False
    childr.valuation = False
    return (childl, childr)

def f_impl(node):
    childl = deepcopy(node.left)
    childr = deepcopy(node.right)
    childl.valuation = True
    childr.valuation = False
    return (childl, childr)

'''
Beta:
    FA ^ B : FA x FB
    TA v B : TA x TB
    TA -> B: FA x TB
'''
def f_and(node):
    childl = deepcopy(node.left)
    childr = deepcopy(node.right)
    childl.valuation = False
    childr.valuation = False
    return (childl, childr)

def t_or(node):
    childl = deepcopy(node.left)
    childr = deepcopy(node.right)
    childl.valuation = True
    childr.valuation = True
    return (childl, childr)

def t_impl(node):
    childl = deepcopy(node.left)
    childr = deepcopy(node.right)
    childl.valuation = False
    childr.valuation = True
    return (childl, childr)
