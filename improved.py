from copy import deepcopy
from node import Node

branches = 0
counter = 0

def start(formulas):
    global counter
    value, brnchs = compute(formulas)
    return (value, brnchs, counter)

def compute(formulas):
    global branches, counter
    for f in formulas:
        print (f)
    print ('\n-------')
    end = expand_alpha(formulas)
    if (end == True or closed(formulas)):
        branches += 1
        return True, branches
    # beta = get_smaller_beta(formulas)
    beta = get_best_beta(formulas)
    if (beta == None):
        branches += 1
        if (not closed(formulas)):
            return get_valuation(formulas), branches
        return True, branches
    else:
        c1, c2 = beta.expand()
        f1, f2 = deepcopy(formulas), deepcopy(formulas)
        f1.append(c1)
        f2.append(c2)
        b1, _ = compute(f1)
        counter += 1
        if (b1 != True):
            return b1, branches
        b2, _ = compute(f2)
        if (b2 != True):
            return b2, branches
        else:
            return True, branches

def expand_alpha(formulas):
    global counter
    for formula in formulas:
        if (formula.is_alpha() and not formula.is_atom() and not formula.expanded):
            c1, c2 = formula.expand()
            counter += 1
            formulas.append(c1)
            if (closed(formulas)): return True
            if (c2 != None):
                formulas.append(c2)
            if (closed(formulas)): return True
    return False

def get_last_beta(formulas):
    for formula in list(reversed(formulas)):
        if (not formula.is_alpha() and formula.expanded == False and not formula.is_atom()):
            return formula
    return None

def get_smaller_beta(formulas):
    # betas = get_betas(formulas)
    betas = formulas
    if (len(betas) == 0): return None
    betas.sort(key=lambda x: x.get_size())
    for beta in betas:
        print ('-- ', beta)
    return betas[0]

def get_best_beta(formulas):
    betas = get_betas(formulas)
    if (len(betas) == 0): return None
    betas_with_subformulas = []
    for i in range(len(betas)):
        beta = deepcopy(betas[i])
        if (has_subformulas(formulas, beta)):
            betas_with_subformulas.append(betas[i])
        # beta1, beta2 = beta.expand()
        # value1, value2 = str(beta1)[1::], str(beta2)[1::]
        # index = list_contains(str_formulas, value1)
        # if (index != -1):
        #     formula = formulas[index]
        #     if (formula.valuation != beta1.valuation):
        #         betas_with_subformulas.append(betas[i])
        # else:
        #     index = list_contains(str_formulas, value2)
        #     if (index != -1):
        #         formula = formulas[index]
        #         if (formula.valuation != beta2.valuation):
        #             betas_with_subformulas.append(betas[i])
    if (len(betas_with_subformulas) == 0):
        return get_smaller_beta(betas)
    elif (len(betas_with_subformulas) == 1):
        return betas_with_subformulas[0]
    else:
        return get_smaller_beta(betas_with_subformulas)

def get_betas(formulas):
    betas = []
    for formula in formulas:
        if (not formula.is_alpha() and formula.expanded == False and not formula.is_atom()):
            betas.append(formula)
    return betas

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

def has_subformulas(formulas, beta):
    if (beta.is_atom()):
        return False
    str_formulas = []
    for i in range(len(formulas)):
        str_formulas.append((i, str(formulas[i])[1::]))
    beta1, beta2 = beta.expand()
    value1, value2 = str(beta1)[1::], str(beta2)[1::]
    index = list_contains(str_formulas, value1)
    if (index != -1):
        formula = formulas[index]
        if (formula.valuation != beta1.valuation):
            return True
    else:
        index = list_contains(str_formulas, value2)
        if (index != -1):
            formula = formulas[index]
            if (formula.valuation != beta2.valuation):
                return True
    return (has_subformulas(formulas, beta1) or has_subformulas(formulas, beta2))

def list_contains(plist, value):
    for (idx, string) in plist:
        if (value == string):
            return idx
    return -1
