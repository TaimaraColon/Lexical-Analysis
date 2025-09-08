import ply.lex as lex

# BEGIN LEXICAL ANALYZER DEFINITION

tokens = ['ID','BLOCK','VAR','ADD','PRINT','VIEW',
          'RUN','MINE','EXPORT','STR','INT','LONG',
          'FLOAT','LIST','TUPLE','DICT','NUM','ASSIGN',
          'TYPEASSIGN','SEPARATOR','LPAREN','RPAREN',
          'NE','LT','GT','LE','GE','PLUS','MINUS','STAR',
          'SLASH','COMMENT','WHITESPACE']

# Dictionary that maps the keyword string to their corresponding token
# keywords = {'block':'BLOCK','var':'VAR','add':'ADD',
#             'print':'PRINT','view':'VIEW','run':'RUN',
#             'mine':'MINE','export':'EXPORT','str':'STR',
#             'int':'INT','long':'LONG','float':'FLOAT',
#             'List':'LIST','Tuple':'TUPLE','Dict':'DICT'}

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

# Keywords
def t_BLOCK(t):  r'block';  return t
def t_VAR(t):    r'var';    return t
def t_ADD(t):    r'add';    return t
def t_PRINT(t):  r'print';  return t
def t_VIEW(t):   r'view';   return t
def t_RUN(t):    r'run';    return t
def t_MINE(t):   r'mine';   return t
def t_EXPORT(t): r'export'; return t
def t_STR(t):    r'str';    return t
def t_INT(t):    r'int';    return t
def t_LONG(t):   r'long';   return t
def t_FLOAT(t):  r'float';  return t
def t_LIST(t):   r'List';   return t
def t_TUPLE(t):  r'Tuple';  return t
def t_DICT(t):   r'Dict';   return t

# PLY uses “longest match”; on ties, the earlier rule wins.
# Since keyword rules are defined above, exact keywords (e.g., "block", "List")
# are matched first; everything else falls through to ID.
def t_ID(t):
    r'[A-Za-z][A-Za-z0-9]*'
    return t

# def t_ID(t):
#     r'[A-Za-z][A-Za-z0-9]*'
#     t.type = keywords.get(t.value, 'ID') # Check if it's a keyword, otherwise assign 'ID'
#     return t

# Handle errors
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