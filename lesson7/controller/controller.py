from model import *

def rational_operation(expression_to_solve: str):
    return rational.evaluate(expression_to_solve)

def complex_operation(a: str, b: str, operation: str):
    return complex.evaluate(a, b, operation)
