from operator import add, mul, sub, truediv as div
import ox

lexer = ox.make_lexer({
    ('MUL', r'\*'),
    ('ADD', r'\+'),
    ('SUB', r'\-'),
    ('DIV', r'\*'),
    ('NUMBER', r'\d+'),
})

def make_ast(src):
    """
        convert soruce code to a list of numbers and operations

        >>>makeast('1 2 +')
        [1.0, 2.0, add]
    """
    tokens = lexer(src)
    return ...

def evaluate (src):
    """
    Avalia o resultado de uma expressao na notacao sufixa
    >>>evaluate('40 2 1 *+')
    42,0
    """
    ast = make_ast(src)
    ...
    return 0.0

while True:
    print('valor:', evaluate(input('expr: ')))