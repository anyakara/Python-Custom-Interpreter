import unittest
from project3 import *
import grin
from interpreter import *
from grinvalues import *
import contextlib
import io
from testing import *

def create_temp_interpreter(testing):
    parsed_grin_statements = list(grin.parse(testing))
    transformed = show_grin_lines(parsed_grin_statements)
    interpreter = GrinInterpreter(transformed)
    interpreter.fetch_and_store_identifiers(transformed)
    return transformed, interpreter

class TestGrinInterpreter(unittest.TestCase):
    def test_fetch_and_store_identifiers(self):
        """testing if identifiers can be stored in namespace beforehand"""
        transformed, interpreter = create_temp_interpreter(testing1)
        interpreter.fetch_and_store_identifiers(transformed)
        self.assertEqual(interpreter._grin_namespace, {'CCZ': 3, 'CZ': 7})

    def test_convert_to_grin_int(self):
        """testing conversion to integers"""
        transformed, interpreter = create_temp_interpreter(testing1)
        value = interpreter.convert_to_grin(5)
        self.assertEqual(value, GrinInt(5))

    def test_convert_to_grin_float(self):
        """testing conversion to floats"""
        transformed, interpreter = create_temp_interpreter(testing1)
        value = interpreter.convert_to_grin(5.5)
        self.assertEqual(value, GrinFloat(5.5))

    def test_convert_to_grin_str(self):
        """testing conversion to strings"""
        transformed, interpreter = create_temp_interpreter(testing1)
        value = interpreter.convert_to_grin("this is a string")
        self.assertEqual(value, GrinStr("this is a string"))

    """def test_store_number_from_input_int(self): # IN-NUM
        transformed, interpreter = create_temp_interpreter(testing17)
        interpreter.store_number_from_input(statement=transformed[0], string=6)
        self.assertEqual(interpreter._grin_namespace, {'X': GrinInt(6)})"""

    """def test_store_number_from_input_float(self): # IN-NUM 2
        transformed, interpreter = create_temp_interpreter(testing18)
        interpreter.store_number_from_input(statement=transformed[0], string=6.6)
        self.assertEqual(interpreter._grin_namespace, {})#, {'X': GrinFloat(6.6)})"""

    def test_store_string_from_input(self): # INSTR
        transformed, interpreter = create_temp_interpreter(testing19)
        interpreter.store_string_from_input(statement=transformed[0], string='string')
        self.assertEqual(interpreter._grin_namespace, {'X': GrinStr('string')})

    def test_update_namespace_constant(self): # LET
        transformed, interpreter = create_temp_interpreter(testing2)
        interpreter.process(1)
        self.assertEqual(interpreter._grin_namespace, {'Z': 5})

    def test_print_value(self): # PRINT
        s = None
        with contextlib.redirect_stdout(io.StringIO()) as redirecting_print_values:
            transformed, interpreter = create_temp_interpreter(testing3)
            interpreter.process(1)
            s = redirecting_print_values.getvalue()
        self.assertEqual(s, '5\n')

    def test_simple_operations_add(self): # ADD
        transformed, interpreter = create_temp_interpreter(testing4)
        interpreter.process(1)
        self.assertEqual(interpreter._grin_namespace, {'A': 9})

    def test_simple_operations_add_w_existing_variable(self): # ADD + VAR in namespace
        transformed, interpreter = create_temp_interpreter(testing15)
        interpreter.process(1)
        self.assertEqual(interpreter._grin_namespace, {'A': 8, 'B': 3})

    def test_simple_operations_sub(self): # SUB
        transformed, interpreter = create_temp_interpreter(testing5)
        interpreter.process(1)
        self.assertEqual(interpreter._grin_namespace, {'A': 2})

    def test_simple_operations_mul(self): # MULT
        transformed, interpreter = create_temp_interpreter(testing6)
        interpreter.process(1)
        self.assertEqual(interpreter._grin_namespace, {'A': 14})

    def test_simple_operations_div(self): # DIV
        transformed, interpreter = create_temp_interpreter(testing7)
        interpreter.process(1)
        self.assertEqual(interpreter._grin_namespace, {'A': 4})

    def test_evaluate_conditional_less_than(self):
        transformed, interpreter = create_temp_interpreter(testing8)
        interpreter.process(1)
        self.assertEqual(interpreter._grin_namespace, {'A': 6})

    def test_jump_to_target(self): # GOTO
        transformed, interpreter = create_temp_interpreter(testing1)
        interpreter.process(1)
        self.assertEqual(interpreter._grin_namespace, {"CCZ": 3, "CZ": 7, "Z": 5, "C": 4})

    def test_execute_subroutine(self): # GO-SUB
        transformed, interpreter = create_temp_interpreter(testing14)
        interpreter.process(1)
        self.assertEqual(interpreter._grin_namespace, {'A': 3})

    """def test_evaluate_conditional_less_than_with_comparison(self):
        transformed, interpreter = create_temp_interpreter(testing20)
        interpreter.evaluate_conditional([True, ])
        self.assertEqual(interpreter._grin_namespace, {"A": 1, "B": 4})"""

if __name__ == "__main__":
    unittest.main()
