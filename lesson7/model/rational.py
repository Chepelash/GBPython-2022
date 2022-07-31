import re
from logger import logger

def evaluate(expression: str):
    def secure_expression(equation: str) -> str:
        token_specification = [
            ("NUMBER", r'(^[+-])?\d+(\.\d*)?'), #integer or decimal
            ("OPERATION", r'[+\-*/]'),
            ("PARENTHESES", r'[()]'), 
            ("SPACES", r'\s'),
            ("MISMATCH", r'.')
        ]
        tok_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in token_specification)
        output_list = []
        for el in re.finditer(tok_regex, equation):
            kind = el.lastgroup
            value = el.group()
            if kind == "MISMATCH":                
                error_text = "Mismatched symbol in expression"                
                raise ValueError(__name__, error_text)
            elif kind == "SPACES":
                continue
            output_list.append(value)
        return "".join(output_list)
    
    def solve(expression: str) -> int:
        secured_expression = secure_expression(expression)
        return eval(secured_expression)

    try:
        result = solve(expression)
    except ZeroDivisionError as e:
        error_text = "Division by zero"
        raise e(__name__, error_text)
    except Exception as e:
        error_text = "Unhandled exception"
        raise Exception(__name__, error_text)
    logger.log_operation(__name__, expression, result)
    return result

