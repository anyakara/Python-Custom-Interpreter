"""
author: @akarra1
purpose: develop a class called grin_manager with a grin_namespace,
methods, helper static methods, and helper simple classes to
process instructions for user.
"""
from grinvalues import *

class GrinTypeError(Exception):
    pass

class GrinInterpreter:
    def __init__(self, processed_lines):
        """Initializing the interpreter's functionality."""
        self._grin_namespace = dict()
        self._grin_parsed_lines = processed_lines

    def fetch_and_store_identifiers(self, transformed):
        """This function is called before process -> as subroutines
        with a particular index have to be processed beforehand."""
        for statement in transformed:
            if statement[1][0].kind().index() == 11:
                self._grin_namespace[statement[1][0].value()] = statement[0]

    @staticmethod
    def convert_to_grin(value):
        """This is a staticmethod to convert any
        string, int, and float into a LET variable."""
        if type(value) == int: return GrinInt(value)
        if type(value) == float: return GrinFloat(value)
        elif type(value) == str: return GrinStr(value)

    def store_number_from_input(self, statement, string=None):
        """Saves the number passed into the grin_token_list.
        Supports 'IN-NUM' functionality."""
        # statement = self.return_statement_void_identifier(statement)
        if string is None: user_input = input()
        else: user_input = string
        try:
            if '.' in user_input:
                user_float = float(user_input)
                self._grin_namespace[statement[1][1].value()] = user_float
            else:
                integer = int(user_input)
                self._grin_namespace[statement[1][1].value()] = integer
        except GrinTypeError as UserInputNotIntOrFloat:
            print(f'Please input an integer or float not string or other type: {UserInputNotIntOrFloat}')

    def store_string_from_input(self, statement, string=None):
        """Saves the string passed into the grin_token_list.
        Supports 'INSTR' functionality."""
        # statement = self.return_statement_void_identifier(statement)
        if string is None: user_input = input()
        else: user_input = string
        try:
            self._grin_namespace[statement[1][1].value()] = user_input
        except BaseException as UserStringInput:
            print(f'Please input string not other type: {UserStringInput}')

    def update_namespace_constant(self, statement):
        """Parsing and store contents for 'LET'."""
        # key, value = self.fetch_key_value(statement)
        if statement[1][1].kind().index() == 11 and statement[1][2].kind().index() == 11: # identifier
            self._grin_namespace[statement[1][1].value()] = self._grin_namespace[statement[1][2].value()]
        elif statement[1][1].kind().index() == 11 and statement[1][2].kind().index() in [18, 19, 20]:
            self._grin_namespace[statement[1][1].value()] = statement[1][2].value()

    def print_value(self, statement):
        """Parse and print for 'PRINT'."""
        if statement[1][1].kind().index() == 11: # identifier
            if statement[1][0].kind().index() == 11:
                return statement[1][3].value()
            key = statement[1][1].value()
            if key in self._grin_namespace.keys():
                print(self._grin_namespace[key])
            else:
                self._grin_namespace[key] = 0
                print(self._grin_namespace[key])
        value = statement[1][1].value()
        _index = statement[1][1].kind().index()
        if _index in [18, 19, 20]:
            print(value)

    def simple_operations(self, statement):
        """Operates on the global grin_namespace, performing one of the four
        operations 'ADD', 'SUB', 'MULT', 'DIV' and calling internal update constant
        function to save that information back into the grin_namespace."""
        # operation, operand, operator
        operator_value = None

        operation, operand, operator = statement[1][0].kind().index(), statement[1][1].value(), statement[1][2].value()
        grin_operand = operand
        if statement[1][2].kind().index() == 11:
            if operator in self._grin_namespace.keys():
                operator_value = self._grin_namespace[operator]
        else:
            operator_value = operator
        grin_operator = self.convert_to_grin(operator_value)
        if operand in self._grin_namespace.keys():
            grin_operand = self._grin_namespace[operand]
        grin_operand = self.convert_to_grin(grin_operand)
        result = operand
        if operation == 1: # ADDITION
            result = grin_operand + grin_operator
        elif operation == 25: # SUBTRACTION
            result = grin_operand - grin_operator
        elif operation == 21: # MULTIPLICATION
            result = grin_operand * grin_operator
        elif operation == 3: # FLOOR DIVISION (DEPENDENT / NON-DEPENDENT ON OPERAND)
            result = grin_operand / grin_operator
        self._grin_namespace[operand] = result

    def evaluate_conditional(self, tuple_obj) -> bool:
        """Evaluates the conditional if there is a conditional in the grin statement."""
        grin_conditional = tuple_obj[2]
        obj1, comparison, obj2 = grin_conditional[1], grin_conditional[2], grin_conditional[3]
        if obj1.kind().index() == 11:
            obj1 = self._grin_namespace[obj1.value()]
        else:
            obj1 = obj1.value()
        if obj2.kind().index() == 11:
            obj2 = self._grin_namespace[obj2.value()]
        else:
            obj2 = obj2.value()
        # comparisons that can be performed
        if comparison.kind().index() == 6: return obj1 == obj2
        elif comparison.kind().index() == 22: return obj1 != obj2
        elif comparison.kind().index() == 9: return obj1 > obj2
        elif comparison.kind().index() == 10: return obj1 >= obj2
        elif comparison.kind().index() == 15: return obj1 < obj2
        elif comparison.kind().index() == 1: return obj1 <= obj2
        elif comparison.kind().index() == 1: return obj1 > obj2
        else: return False

    def jump_index(self, statement):
        """Returns the jump index for jumps and subroutines."""
        if statement[1][1].kind().index() == 11:  # identifier
            if self._grin_namespace[statement[1][1].value()] in self._grin_namespace.keys():
                return self._grin_namespace[self._grin_namespace[statement[1][1].value()]]
            elif type(self._grin_namespace[statement[1][1].value()]) == int:
                target = self._grin_namespace[statement[1][1].value()] + statement[0]
                return target
        elif statement[1][1].kind().index() == 20:  # string literal
            return self._grin_namespace[statement[1][1].value()]
        elif statement[1][1].kind().index() == 19: # integer
            return statement[0] + statement[1][1].value() # offset by 1 unit

    @staticmethod
    def check_with_conditional(statement):
        """Checks if a conditional is present in GO-TO or GO-SUB routine call."""
        if len(statement[1]) > 2:
            if statement[1][2].kind().index() == 12:
                return tuple([True, statement[1][:2], statement[1][2:]])
        return tuple([False, statement, None])

    def jump_to_target(self, statement):
        """Fetches jump index to execute a jump statement."""
        with_conditional, grin_line, grin_conditional = self.check_with_conditional(statement)
        if with_conditional:
            tuple_obj = tuple([with_conditional, grin_line, grin_conditional])
            if self.evaluate_conditional(tuple_obj):
                return self.jump_index(statement)
            return None
        return self.jump_index(statement)


    def evaluate_for_subroutine(self, statement):
        """Evaluates for subroutine options, including identifiers,
        literal strings, and literal integers."""
        if statement[1][1].kind().index() == 11: # identifier
            self.process(start_index=self._grin_namespace[statement[1][1].value()])
        elif statement[1][1].kind().index() == 20: # literal string
            self.process(start_index=self._grin_namespace[statement[1][1].value()])
        elif statement[1][1].kind().index() == 19: # literal integer
            self.process(start_index=statement[1][1].value() + statement[0])
        return statement[0]

    def execute_subroutine(self, statement):
        """Evaluate subroutines by calling process function with the execute subroutine function."""
        with_conditional, grin_line, grin_conditional = self.check_with_conditional(statement)
        if with_conditional:
            tuple_obj = tuple([with_conditional, grin_line, grin_conditional])
            if self.evaluate_conditional(tuple_obj):
                return self.evaluate_for_subroutine(statement)
            return None
        return self.evaluate_for_subroutine(statement)

    @staticmethod
    def checking_for_routine_labels(statement):
        """Removing the identifier and colon tags if they are present. (This is done
        because identifiers and line numbers have been previously already stored.)"""
        if len(statement[1]) > 2:
            if statement[1][1].text() == ':':
                return [statement[0], statement[1][2:]]
        return statement

    def process(self, start_index=None):
        """Process function executes the process with the start index given. The two
        ways the process function breaks is if the program ending is caught, or the program
        subroutine has finished executing (encounters a RETURN statement)."""
        index = start_index
        while 0 <= index <= len(self._grin_parsed_lines):
            statement = self.checking_for_routine_labels(self._grin_parsed_lines[index-1])
            call = statement[1][0].kind().index()
            if call == 17: # LET
                self.update_namespace_constant(statement)
            elif call == 13: # IN-NUM
                self.store_number_from_input(statement)
            elif call == 14: # INSTR
                self.store_string_from_input(statement)
            elif call == 23: # PRINT
                self.print_value(statement)
            elif call in [1, 25, 21, 3]: # ARITHMETIC
                self.simple_operations(statement)
            elif call == 5: # END
                break
            elif call == 8: # JUMPING W/OUT CONDITIONALS
                index = self.jump_to_target(statement) - 1
            elif call == 7: # SUBROUTINE W/OUT CONDITIONALS
                index = self.execute_subroutine(statement)
            elif call == 24: # RETURN
                break
            index += 1

__all__ = [GrinInterpreter.__name__]
