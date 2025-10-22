class AST:
    pass

class Print(AST):
    def __init__(self, values):
        self.values = values

class String(AST):
    def __init__(self, value):
        self.value = value

class Number(AST):
    def __init__(self, value):
        self.value = value

class Variable(AST):
    def __init__(self, name):
        self.name = name

class Input(AST):
    def __init__(self, variable):
        self.variable = variable
