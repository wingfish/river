# import pandas as pd
#
# ser1 = pd.Series([1.5, 2.5, 3, 4.5, 5.0, 6])
# print(ser1)

from prompt_toolkit import prompt
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style

import pygments
from pygments.lexers.python import PythonLexer

from prompt_toolkit.formatted_text import PygmentsTokens
from prompt_toolkit import print_formatted_text

print_formatted_text(HTML('<b>This is bold</b>'))
print_formatted_text(HTML('<i>This is italic</i>'))
print_formatted_text(HTML('<u>This is underlined</u>'))
print_formatted_text(HTML('<aaa fg="ansiwhite" bg="ansigreen">White on green</aaa>'))

# The text.
text = FormattedText([
    ('class:aaa', 'Hello'),
    ('', ' '),
    ('class:bbb', 'World'),
])

# The style sheet.
style = Style.from_dict({
    'aaa': '#ff0066',
    'bbb': '#44ff00 italic',
})

print_formatted_text(text, style=style)

s = 'def a():' \
    '   for i in range(10):' \
    '       print(i)'

tokens = list(pygments.lex(s, lexer=PythonLexer()))
print(tokens)
print_formatted_text(PygmentsTokens(tokens))

text = prompt('Give me some input: ')
print('You said: %s' % text)
