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
    # for formula in formulas:
    #     print ('X ' if formula.expanded else '  ', str(formula))
    end = expand_alpha(formulas)
    # print ('----------------------------------\n')
    if (end == True or closed(formulas)):
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
        f1, f2 = deepcopy(formulas), deepcopy(formulas)
        f1.append(c1)
        f2.append(c2)
        b1 = compute(f1)
        counter += 1
        if (b1 != True):
            return b1
        b2 = compute(f2)
        counter += 1
        if (b2 != True):
            return b2
        else:
            return True

def expand_alpha(formulas):
    global counter
    for formula in formulas:
        if (formula.is_alpha() and not formula.is_atom() and not formula.expanded):
            c1, c2 = formula.expand()
            counter += 1
            formulas.append(c1)
            # print (c1)
            if (closed(formulas)): return True
            if (c2 != None):
                counter += 1
                # print (c2)
                formulas.append(c2)
            if (closed(formulas)): return True
    return False

def get_last_beta(formulas):
    for formula in list(reversed(formulas)):
        if (not formula.is_alpha() and formula.expanded == False and not formula.is_atom()):
            return formula
    return None

def closed(formulas):
    last_atom = formulas[len(formulas)-1]
    if (has_absurd(last_atom, formulas)):
        return True
    else:
        return False

def has_absurd(atom, formulas):
    for i in range(len(formulas) - 1):
        formula = formulas[i]
        if (formula.is_atom() and not formula.expanded):
            if (atom.token == formula.token):
                if (atom.valuation != formula.valuation):
                    return True
    return False

def get_valuation(formulas):
    valuation = []
    for f in formulas:
        if (f.is_atom()):
            valuation.append('{}: {}'.format(f.token, f.valuation))
    return valuation
