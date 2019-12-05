
INTEGER, PLUS, MINUS, EOF = "INTEGER", "PLUS", "MINUS", "EOL"


class Token:

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"

    def __repr__(self):
        return self.__str__()


class Interpreter:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = text[self.pos]

    def error(self):
        raise Exception("Error parsing input")

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

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()

            if self.current_char is None:
                return(EOF, None)

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            
            elif self.current_char in ["+", "-"]:
                op = self.current_char
                self.advance()
                return Token(PLUS, op)
            
            else:
                self.error()
        return Token(EOF, None)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token() 
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()
        left = self.current_token.value
        self.eat(INTEGER)
        op = self.current_token.value
        self.eat(PLUS)
        right = self.current_token.value
        self.eat(INTEGER)
        return eval(str(left) + op +  str(right))


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()