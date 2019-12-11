
TOKEN_DICT = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "MUL",
    "/": "DIV",
    "(": "LPAREN",
    ")": "RPAREN",
    "EOF": None,
    "INTEGER": lambda x:x
}

class Token:

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token {self.type}, {self.value}"

    def __repr__(self):
        return self.__str__()


class Lexer:

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception("error")

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def integer(self):
        result = "" 
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            elif self.current_char.isdigit():
                return Token("INTEGER", self.integer())
            else:
                token = self.current_char
                self.advance()
                return Token(TOKEN_DICT.get(token), token)
        return Token("EOF", None)

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()


class Interpreter:

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self):
        self.current_token = self.lexer.get_next_token()

    def factor(self):
        token = self.current_token
        if token.type == "INTEGER":
            self.eat()
            return token.value
        if token.type == "LPAREN":
            self.eat()
            reslut = self.expr()
            self.eat()
            return reslut

    def term(self):
        result = self.factor()
        while self.current_token.type in ("DIV", "MUL"):
            token = self.current_token
            op = token.value
            self.eat()
            right = str(self.factor())
            result = eval(str(result) + str(op) + str(right))
        return result

    def expr(self):
        result = self.term()
        while self.current_token.type in ("PLUS", "MINUS"):
            token = self.current_token
            self.eat()
            op = token.value
            right = self.term() 
            result = eval(str(result) + str(op) + str(right))

        return result


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()