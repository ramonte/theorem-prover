import expansions

class Node:
    def __init__(self, token, left = None, right = None):
        self.token = token
        self.left = left
        self.right = right
        self.valuation = None
        self.expanded = False

    def is_alpha(self):
        if (self.valuation == True):
            return (self.token == '-' or self.token == '*')
        else:
            return (self.token == '-' or self.token == '+' or self.token == ')')

    def is_atom(self):
        return not (self.token == ')' or self.token == '*' or self.token == '+' or self.token == '-')

    def get_size(self):
        size = 1
        if (self.right != None):
            size += self.right.get_size()
        if (self.left != None):
            size += self.left.get_size()
        return size

    def expand(self):
        self.expanded = True
        if (self.token == ')'):
            if (self.valuation == True):
                return expansions.t_impl(self)
            else:
                return expansions.f_impl(self)
        elif (self.token == '*'):
            if (self.valuation == True):
                return expansions.t_and(self)
            else:
                return expansions.f_and(self)
        elif (self.token == '+'):
            if (self.valuation == True):
                return expansions.t_or(self)
            else:
                return expansions.f_or(self)
        elif (self.token == '-'):
            if (self.valuation == True):
                return expansions.t_neg(self)
            else:
                return expansions.f_neg(self)
        else:
            raise Exception('Um átomo não pode ser expandido.')

    def str_token(self):
        if (self.token == ')'):
            return '->'
        elif (self.token == '*'):
            return '^'
        elif (self.token == '+'):
            return 'v'
        elif (self.token == '-'):
            return '¬'
        else:
            return self.token

    def __str__(self):
        r = ''
        if (self.valuation == True):
            r += 'T'
        elif (self.valuation == False):
            r += 'F'
        if (self.left):
            r += '(' + str(self.left)
        r += self.str_token()
        if (self.right):
            r += str(self.right)
            if (self.token != '-'):
                r += ')'
        return r
