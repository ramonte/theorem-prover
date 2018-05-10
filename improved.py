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
    # beta = get_best_beta(formulas)
    beta = get_smaller_beta(get_betas(formulas))
    if (beta == None):
        branches += 1
        if (not closed(formulas)):
            return get_valuation(formulas)
        return True
    else:
        c1, c2 = beta.expand()
        f1, f2 = deepcopy(formulas), deepcopy(formulas)
        if (not exists(c1, formulas)):
            f1.append(c1)
            counter += 1
            b1 = compute(f1)
            if (b1 != True):
                return b1
        if (not exists(c2, formulas)):
            f2.append(c2)
            counter += 1
            b2 = compute(f2)
            if (b2 != True):
                return b2
            else:
                return True
        return True

def expand_alpha(formulas):
    global counter
    for formula in formulas:
        if (formula.is_alpha() and not formula.is_atom() and not formula.expanded):
            c1, c2 = formula.expand()
            if (not exists(c1, formulas)):
                # print (str(c1))
                counter += 1
                formulas.append(c1)
            if (closed(formulas)): return True
            if (c2 != None):
                if (not exists(c2, formulas)):
                    # print (str(c2))
                    counter += 1
                    formulas.append(c2)
            if (closed(formulas)): return True
    return False

def get_last_beta(formulas):
    for formula in list(reversed(formulas)):
        if (not formula.is_alpha() and formula.expanded == False and not formula.is_atom()):
            return formula
    return None

def get_smaller_beta(formulas):
    betas = formulas
    if (len(betas) == 0): return None
    sbetas = sorted(betas, key=lambda x: x.get_size())
    # if (len(sbetas) > 1):
        # if (sbetas[0].get_size() == sbetas[1].get_size()):
            # return None
    return betas[0]

def get_best_beta(formulas):
    betas = get_betas(formulas)
    if (len(betas) == 0): return None
    betas_with_subformulas = []
    for i in range(len(betas)):
        beta = deepcopy(betas[i])
        if (has_subformulas(formulas, beta)):
            betas_with_subformulas.append(betas[i])
    if (len(betas_with_subformulas) == 0):
        smaller = get_smaller_beta(betas)
        if (smaller != None):
            return smaller
        else:
            return get_last_beta(formulas)
    elif (len(betas_with_subformulas) == 1):
        return betas_with_subformulas[0]
    else:
        # return get_smaller_beta(betas_with_subformulas)
        smaller = get_smaller_beta(betas_with_subformulas)
        if (smaller != None):
            return smaller
        else:
            return get_last_beta(formulas)

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
    if (not beta1.is_atom() and not beta1.is_alpha()):
        if (not beta2.is_atom() and not beta2.is_alpha()):
            return (has_subformulas(formulas, beta1) or has_subformulas(formulas, beta2))
        else:
            return (has_subformulas(formulas, beta1))
    elif (not beta2.is_atom() and not beta2.is_alpha()):
        return (has_subformulas(formulas, beta2))
    else:
        return False

def exists(child, formulas):
    for f in formulas:
        if (str(child) == str(f)):
            return True
    return False

def list_contains(plist, value):
    for (idx, string) in plist:
        if (value == string):
            return idx
    return -1
