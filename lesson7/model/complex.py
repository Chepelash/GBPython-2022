from logger import logger


def evaluate(a: str, b: str, operation: str):
    def solve(a_num: complex, b_num: complex, operation_index: int):
        if operation_index == 1:
            result = a_num + b_num
            logger.log_operation(__name__, f"{a_num} + {b_num}", result)
            return result
        elif operation_index == 2:
            result = a_num - b_num
            logger.log_operation(__name__, f"{a_num} - {b_num}", result)
            return result
        elif operation_index == 3:
            result = a_num * b_num
            logger.log_operation(__name__, f"{a_num} * {b_num}", result)
            return result
        elif operation_index == 4:
            result = a_num / b_num
            logger.log_operation(__name__, f"{a_num} / {b_num}", result)
            return result
        else:
            raise NotImplementedError(__name__, "Operation is not implemented")

    if not str.isdigit(operation):
        raise ValueError(__name__, "Operation is not a number")
    operation_index = int(operation)

    # Exceptions
    try:
        a_num = complex(a)
        b_num = complex(b)
    except ValueError:
        raise ValueError(__name__, "Numbers are not complex")
    try:
        return solve(a_num, b_num, operation_index)
    except NotImplementedError as e:
        raise e
    except Exception:
        raise Exception(__name__, "Unhandled exception")

    