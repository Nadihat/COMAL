
import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []
        self.current_pos = 0

    def tokenize(self):
        while self.current_pos < len(self.code):
            # Skip whitespace
            if self.code[self.current_pos].isspace():
                self.current_pos += 1
                continue

            # Match keywords, identifiers, numbers, strings, and operators
            match = re.match(r'\b(PRINT|INPUT|IF|THEN|ELSE|ENDIF|FOR|TO|STEP|NEXT|WHILE|ENDWHILE|PROC|ENDPROC|DIM)\b', self.code[self.current_pos:])
            if match:
                self.tokens.append(Token('KEYWORD', match.group(1)))
                self.current_pos += len(match.group(1))
                continue

            match = re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', self.code[self.current_pos:])
            if match:
                self.tokens.append(Token('IDENTIFIER', match.group(0)))
                self.current_pos += len(match.group(0))
                continue

            match = re.match(r'\d+(\.\d+)?', self.code[self.current_pos:])
            if match:
                self.tokens.append(Token('NUMBER', float(match.group(0))))
                self.current_pos += len(match.group(0))
                continue

            match = re.match(r'"[^"]*"', self.code[self.current_pos:])
            if match:
                self.tokens.append(Token('STRING', match.group(0)[1:-1]))
                self.current_pos += len(match.group(0))
                continue

            match = re.match(r'<>|<=|>=|<|>|=|\+|-|\*|/|\(|\)|,', self.code[self.current_pos:])
            if match:
                self.tokens.append(Token('OPERATOR', match.group(0)))
                self.current_pos += len(match.group(0))
                continue

            raise Exception(f"Invalid character: {self.code[self.current_pos]}")

        return self.tokens
