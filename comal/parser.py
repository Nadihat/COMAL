from comal.ast import Print, String, Input, Variable

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def parse(self):
        statements = []
        while self.current_token_index < len(self.tokens):
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        token = self.tokens[self.current_token_index]
        if token.type == 'KEYWORD' and token.value == 'PRINT':
            return self.parse_print_statement()
        elif token.type == 'KEYWORD' and token.value == 'INPUT':
            return self.parse_input_statement()
        else:
            raise Exception(f"Invalid statement: {token}")

    def parse_print_statement(self):
        self.current_token_index += 1  # Consume PRINT token
        values = []
        while self.current_token_index < len(self.tokens):
            token = self.tokens[self.current_token_index]
            if token.type == 'STRING':
                values.append(String(token.value))
                self.current_token_index += 1
            elif token.type == 'IDENTIFIER':
                values.append(Variable(token.value))
                self.current_token_index += 1
            else:
                raise Exception(f"Invalid print statement: {token}")

            if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index].type == 'OPERATOR' and self.tokens[self.current_token_index].value == ',':
                self.current_token_index += 1  # Consume comma
            else:
                break
        return Print(values)

    def parse_input_statement(self):
        self.current_token_index += 1  # Consume INPUT token
        token = self.tokens[self.current_token_index]
        if token.type == 'IDENTIFIER':
            self.current_token_index += 1  # Consume IDENTIFIER token
            return Input(Variable(token.value))
        else:
            raise Exception(f"Invalid input statement: {token}")
