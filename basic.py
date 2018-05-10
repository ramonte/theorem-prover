from copy import deepcopy
from node import Node

branches = 0
counter = 0

def start(formulas):
    global counter
    counter = len(formulas)
    value = compute(formulas)
    return (value, branches, counter)

def compute(formulas):
    global branches, counter
    if (closed(formulas)):
        branches += 1
        return True
    end = expand_alpha(formulas)
    if (end == True):
        branches += 1
        return True
    beta = get_last_beta(formulas)
    if (beta == None):
        branches += 1
        if (not closed(formulas)):
            return get_valuation(formulas)
        return True
    else:
        c1, c2 = beta.expand()
        new_branch = deepcopy(formulas)
        formulas.append(c1)
        new_branch.append(c2)
        branch1 = compute(formulas)
        counter += 1
        if (branch1 != True):
            return branch1
        branch2 = compute(new_branch)
        counter += 1
        if (branch2 != True):
            return branch2
        else:
            return True

def expand_alpha(formulas):
    global counter
    for formula in formulas:
        if (formula.is_alpha() and not formula.is_atom() and not formula.expanded):
            c1, c2 = formula.expand()
            counter += 1
            formulas.append(c1)
            if (closed(formulas)): return True
            if (c2 != None):
                counter += 1
                formulas.append(c2)
            if (closed(formulas)): return True
    return False

def get_last_beta(formulas):
    for formula in list(reversed(formulas)):
        if (not formula.is_alpha() and formula.expanded == False and not formula.is_atom()):
            return formula
    return None

def closed(formulas):
    last_formula = formulas[len(formulas)-1]
    if (has_absurd(last_formula, formulas)):
        return True
    else:
        return False

def has_absurd(atom, formulas):
    for i in range(len(formulas) - 1):
        formula = formulas[i]
        if (str(formula)[1:] == str(atom)[1:]):
            if (atom.valuation != formula.valuation):
                return True
    return False

def get_valuation(formulas):
    valuation = []
    for f in formulas:
        if (f.is_atom()):
            valuation.append('{}: {}'.format(f.token, f.valuation))
    return valuation

def remove_expanded(formulas):
    new_list = []
    for formula in formulas:
        if (formula.expanded == False):
            new_list.append(formula)
    return new_list
