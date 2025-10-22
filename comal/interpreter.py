from comal.lexer import Lexer
from comal.parser import Parser
from comal.evaluator import Evaluator

class Interpreter:
    def __init__(self, code):
        self.code = code

    def run(self):
        lexer = Lexer(self.code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        evaluator = Evaluator(ast)
        evaluator.evaluate()

