class Node:

    def __init__(self, token, left = None, right = None):
        self.token = token
        self.left = left
        self.right = right

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
        if (self.left):
            r += '(' + str(self.left)
        r += self.str_token()
        if (self.right):
            r += str(self.right) + ')   '
        return r
