"""
B. Значение выражения
ограничение по времени на тест2 секунды
ограничение по памяти на тест64 мегабайта
вводстандартный ввод
выводстандартный вывод
Задано числовое выражение, заканчивающееся точкой. Необходимо посчитать его значение или сказать, что оно содержит ошибку. В выражении могут встречаться знаки сложения, вычитания, умножения и скобки. Приоритет операций стандартный. Все числа в выражении целые и принадлежат диапазону LongInt. Также гарантируется, что все промежуточные вычисления умещаются в этот тип. Унарный плюс и унарный минус в выражении встречаться не могут, как и два знака подряд.

Входные данные
Первая строка содержит заданное выражение. Его длина не превосходит 100 знаков. Гарантируется, что выражение заканчивается точкой.

Выходные данные
Выведите значение этого выражения или слово «WRONG», если значение не определено.

Примеры
входные данныеСкопировать
1+(2*2-3).
выходные данныеСкопировать
2
входные данныеСкопировать
1+a+1.
выходные данныеСкопировать
WRONG

"""
class Lexer:
    """
    Lexer for arythmetic expressions
    """
    DIGITS = {str(x) for x in range(0, 10)}
    ADD_OPERATIONS = {"+", "-"}
    MUL_OPERATIONS = {"*", "/"}
    LP = "("
    RP = ")"
    END = "."
    IGNORE = {' '}
    NUM_T = "number"
    ADD_OP_T = "additive_operation"
    MUL_OP_T = "multiplicative_operation"
 
    def __init__(self, text):
        self.lexemes = Lexer.get_lexemes(text)
        self.next_id = 0
        self.n_lexemes = len(self.lexemes)
 
    @staticmethod
    def get_lexemes(text):
        """
        Extracts list of exemes from string with arithmetic
        :param text: text of arithmetic expression
        :return: list of lexemes
        """
        lexemes = []
        token_buff: str = ""
        found_dot = False
 
        for pos, char in enumerate(text):
            if char in Lexer.DIGITS:
                token_buff += char
            else:
                if len(token_buff) > 0:
                    lexemes.append((int(token_buff), Lexer.NUM_T))
                    token_buff = ""
                if char == Lexer.END and not found_dot:
                    found_dot = True  # TODO: maybe it's a bad idea
                    lexemes.append((char, Lexer.END))
                elif char in Lexer.ADD_OPERATIONS and not found_dot:
                    lexemes.append((char, Lexer.ADD_OP_T))
                elif char in Lexer.MUL_OPERATIONS and not found_dot:
                    lexemes.append((char, Lexer.MUL_OP_T))
                elif char == Lexer.LP and not found_dot:
                    lexemes.append((char, Lexer.LP))
                elif char == Lexer.RP and not found_dot:
                    lexemes.append((char, Lexer.RP))
                elif char in Lexer.IGNORE:
                    continue
                else:
                    msg = f"Unexpected symbol: {char}"
                    raise Exception(msg)
        if len(token_buff) > 0:
            lexemes.append((int(token_buff), Lexer.NUM_T))
        if found_dot:
            return lexemes
        else:
            raise Exception()
 
    def has_tokens(self):
        """
        Checks if Lexer has tokens to iterate
        :return: True if next_token can return lexemes, False in other case
        """
        return self.next_id < self.n_lexemes
 
    def next_token(self):
        """
        Iterates over lexemes
        :return: next token
        """
        if self.has_tokens():
            result = self.lexemes[self.next_id]
            self.next_id += 1
        else:
            result = None
        return result
 
 
class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.cache = {}
        self.parenthesis_balance = 0
        if lexer.has_tokens():
            self.curr_value, self.curr_type = self.lexer.next_token()
            if self.curr_type in {Lexer.LP, Lexer.NUM_T}:
                self.ret_value = None
                self.value = self.parse_expression()
                if self.lexer.has_tokens() or self.curr_type != Lexer.END or self.parenthesis_balance != 0:
                    raise Exception("Expected end of expression.")
            else:
                raise Exception(
                    f"Unexpected beginning of the expression: {(self.curr_type, self.curr_type)}")
 
    def parse_expression(self):
        result = None
        if self.lexer.has_tokens():
            result = self.parse_term()
            is_exit = not self.lexer.has_tokens()
            while not is_exit:
                if self.curr_type == Lexer.ADD_OP_T:
                    op = self.curr_value
                    self.curr_value, self.curr_type = self.lexer.next_token()
                    term = self.parse_term()
                    if op == '+':
                        result += term
                    else:
                        result -= term
                elif self.curr_type == Lexer.NUM_T:
                    raise Exception(
                        f"Number is not expected: {(self.curr_type, self.curr_type)}")
                else:
                    is_exit = True
        elif self.curr_type == Lexer.NUM_T:
            result = self.curr_value
        else:
            raise Exception(
                f"Unexpected beginning of the expression: {(self.curr_type, self.curr_type)}")
        return result
 
    def parse_term(self):
        result = self.parse_factor()
        is_exit = not self.lexer.has_tokens()
        while not is_exit:
            if self.curr_type == Lexer.MUL_OP_T:
                op = self.curr_value
                self.curr_value, self.curr_type = self.lexer.next_token()
                term = self.parse_factor()
                if op == "*":
                    result *= term
                else:
                    result /= term
            else:
                is_exit = True
        return result
 
    def parse_factor(self):
        if self.curr_value == self.lexer.LP:
            self.curr_value, self.curr_type = self.lexer.next_token()
            result = self.parse_expression()
            self.parenthesis_balance += 1
            if self.curr_value == self.lexer.RP:
                self.parenthesis_balance -= 1
        else:
            result = self.curr_value
            self.curr_value = None
            self.curr_type = None
        if self.lexer.has_tokens():
            self.curr_value, self.curr_type = self.lexer.next_token()
        return result
 
    def get_result(self):
        return self.value
 
 
def main():
    try:
        lexer = Lexer(input())
        parser = Parser(lexer)
        print(parser.get_result())
    except Exception:
        print("WRONG")
 
 
def test():
    """
    Examples:
    ). -> WRONG
    1. -> 1
    (8-3+2. -> WRONG
    (1)2. -> WRONG
    (((1))). -> 1
    2-(2+2) -> -2
    2+2/2-2 -> -1
    :return:
    """
    lexer = Lexer(").")
    parser = Parser(lexer)
    print(parser.get_result())
 
 
if __name__ == '__main__':
    main()
