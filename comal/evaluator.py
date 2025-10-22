from comal.ast import Print, String, Input, Variable

class Evaluator:
    def __init__(self, ast):
        self.ast = ast
        self.variables = {}

    def evaluate(self):
        for node in self.ast:
            self.evaluate_node(node)

    def evaluate_node(self, node):
        if isinstance(node, Print):
            self.evaluate_print(node)
        elif isinstance(node, Input):
            self.evaluate_input(node)
        else:
            raise Exception(f"Invalid node: {node}")

    def evaluate_print(self, node):
        values = []
        for value in node.values:
            if isinstance(value, String):
                values.append(value.value)
            elif isinstance(value, Variable):
                if value.name in self.variables:
                    values.append(self.variables[value.name])
                else:
                    raise Exception(f"Undefined variable: {value.name}")
            else:
                raise Exception(f"Invalid print value: {value}")
        print(*values)

    def evaluate_input(self, node):
        if isinstance(node.variable, Variable):
            value = input()
            self.variables[node.variable.name] = value
        else:
            raise Exception(f"Invalid input variable: {node.variable}")
