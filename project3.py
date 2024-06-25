# project3.py
#
# ICS 33 Spring 2023
# Project 3: Why Not Smile?
#
# The main module that executes your Grin interpreter.
#
# WHAT YOU NEED TO DO: You'll need to implement the outermost shell of your
# program here, but consider how you can keep this part as simple as possible,
# offloading as much of the complexity as you can into additional modules in
# the 'grin' package, isolated in a way that allows you to unit test them.

import grin
from interpreter import *
import grin

def _obtain_input() -> list:
    """Obtains grin statements and returns
    them to main. These values are processed as lists."""
    grin_statements = list()
    while True:
        statement = input()
        if '.' == statement.strip():
            grin_statements.append('.')
            break
        grin_statements.append(statement)
    return grin_statements

def show_grin_lines(grin_lines):
    """Transforming grin lines to have custom line numbers
    that are used extensively in the interpreter's inner methods."""
    transformed = list()
    counter = 1
    for statement in grin_lines:
        transformed.append([counter, [token for token in statement]])
        counter += 1
    return transformed

def main() -> None:
    """Main engine of the grin program inputs. If tokens cannot be parsed
    a GrinParseError is returned."""
    grin_statements = _obtain_input()
    try:
        parsed_grin_statements = list(grin.parse(grin_statements))
        transformed = show_grin_lines(parsed_grin_statements)
        grin_interpreter = GrinInterpreter(transformed)
        grin_interpreter.fetch_and_store_identifiers(transformed)
        grin_interpreter.process(1)
    except grin.GrinParseError as E:
        print("Could not parse because of these reasons:", E)


if __name__ == '__main__':
    main()
