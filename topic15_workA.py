"""
A. Разделение выражения на лексемы
ограничение по времени на тест1 секунда
ограничение по памяти на тест256 мегабайт
вводстандартный ввод
выводстандартный вывод
Задано числовое выражение, заканчивающееся точкой. Необходимо разбить его на лексемы и вывести каждую на новой строке. Гарантируется, что исходное выражение корректно.

В выражении могут встречаться знаки сложения, вычитания, умножения и скобки. Приоритет операций стандартный. Все числа в выражении целые и принадлежат диапазону LongInt.

Входные данные
Первая строка содержит заданное выражение. Его длина не превосходит 100 знаков. Гарантируется, что выражение заканчивается точкой.

Выходные данные
Выведите все встречающиеся лексемы выражения по порядку и ровно по одной на каждой строке.

Пример
входные данныеСкопировать
1+(2*2-3).
выходные данныеСкопировать
1
+
(
2
*
2
-
3
)

"""

class Lexer:
    """
    Lexer for arythmetic expressions
    """
    DIGITS = {str(x) for x in range(0, 10)}
    OPERATIONS = {"+", "-", "*", "/"}
    PARENTHESES = {"(", ")"}
    END = "."
    IGNORE = {' '}
 
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
        for char in text:
            if char in Lexer.DIGITS:
                token_buff += char
            else:
                if len(token_buff) > 0:
                    lexemes.append(token_buff)
                    token_buff = ""
                if char == Lexer.END:
                    break  # TODO: maybe it's a bad idea
                elif (char in Lexer.OPERATIONS) or (char in Lexer.PARENTHESES):
                    lexemes.append(char)
                elif char in Lexer.IGNORE:
                    continue
                else:
                    msg = f"Unexpected symbol: {char}"
                    raise Exception(msg)
        return lexemes
 
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
 
 
def main():
    string: str = input()
    lexer = Lexer(string)
    while lexer.has_tokens():
        print(lexer.next_token())
 
 
if __name__ == '__main__':
    main()