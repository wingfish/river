from prompt_toolkit import PromptSession
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import PygmentsTokens

import pygments
from pygments.lexers.python import PythonLexer

from pathlib import Path

from cmd import hello


# The style sheet.
style = Style.from_dict({
    'info': '#99FF00'
})

# The text.
TEXT_WELCOME = FormattedText([
    ('class:info', 'Hello, welcome to River Shell, use CTRL+D exit'),
])

TEXT_GOODBYE = FormattedText([
    ('class:info', 'Goodbye!'),
])

print_formatted_text(TEXT_WELCOME, style=style)

# 命令建议
my_completer = WordCompleter([
    'show', 'byebye', 'help', 'hello'], ignore_case=True)


def do_command(keyword, cmd):
    if keyword == 'show':
        filename = cmd.split()[1]
        print(filename)
        print(Path.cwd())
        file = Path.cwd() / Path(filename)
        print(file)

        if Path(file).exists():
            print('file exists')

            print('-'*20)
            tokens = list(pygments.lex(Path(file).read_text(), lexer=PythonLexer()))
            print_formatted_text(PygmentsTokens(tokens))

        else:
            print('file not exists')
    elif keyword == 'hello':
        args = cmd.split(' ')
        print(args)
        # delete first command
        print(tuple(args[1:]))
        hello(tuple(args[1:]))
    elif keyword == 'help':
        print('HELP')


def main():
    session = PromptSession(completer=my_completer)

    while True:
        try:
            cmd = session.prompt('> ')
        except KeyboardInterrupt:
            continue
        except EOFError:
            break
        # 输入正确命令进行解析
        else:
            print('You entered:', cmd)
            keyword = cmd.split()[0]
            do_command(keyword, cmd)

    print_formatted_text(TEXT_GOODBYE, style=style)


if __name__ == '__main__':
    main()
