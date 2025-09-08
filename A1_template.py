import ply.lex as lex

# BEGIN LEXICAL ANALYZER DEFINITION

tokens = ['ID','BLOCK','VAR','ADD','PRINT','VIEW',
          'RUN','MINE','EXPORT','STR','INT','LONG',
          'FLOAT','LIST','TUPLE','DICT','NUM','ASSIGN',
          'TYPEASSIGN','SEPARATOR','LPAREN','RPAREN',
          'NE','LT','GT','LE','GE','PLUS','MINUS','STAR',
          'SLASH','COMMENT','WHITESPACE']

# Dictionary that maps the keyword string to their corresponding token
keywords = {'block':'BLOCK','var':'VAR','add':'ADD',
            'print':'PRINT','view':'VIEW','run':'RUN',
            'mine':'MINE','export':'EXPORT','str':'STR',
            'int':'INT','long':'LONG','float':'FLOAT',
            'List':'LIST','Tuple':'TUPLE','Dict':'DICT'}

# Ignore comments
def t_COMMENT(t):
    r'//[^\n]*'
    t.lexer.lineno += t.value.count('\n')
    pass

# Ignore whitespaces
def t_WHITESPACE(t):
    r'[ \t\r\n]+'
    t.lexer.lineno += t.value.count('\n')
    pass

# Token matching rules are written as regexs
t_SEPARATOR = r','
t_ASSIGN = r'='
t_TYPEASSIGN = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NE = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_PLUS = r'\+'
t_MINUS = r'-'
t_STAR = r'\*'
t_SLASH = r'/'
t_NUM = r'[0-9]+'

def t_ID(t):
    r'[A-Za-z][A-Za-z0-9]*'
    # Check if it's a keyword, otherwise stays 'ID'
    t.type = keywords.get(t.value, 'ID') 
    return t

# Handle errors and specifies in which row
def t_error(t):
    print(f'Illegal character {t.value[0]!r} in row {t.lexer.lineno}')
    t.lexer.skip(1)

# END LEXICAL ANALYZER DEFINITION


#Testing Lexical Analysis
lexer = lex.lex()
 
textFile = open('Program_Test.txt', 'r')

data = textFile.read()

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)