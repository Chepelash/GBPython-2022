import os
from datetime import datetime as dt

PATH_TO_LOG_FILE = os.path.join("..", "log.txt")
DATETIME_FORMAT = "%Y %m %d %H:%M:%S"


def log_operation(module_name: str, request: str, result: str):
    with open(PATH_TO_LOG_FILE, 'a') as f:
        f.write(f"{dt.now().strftime(DATETIME_FORMAT)} {module_name}: request {request} -> {result}")

def log_error(module_name: str, error_text: str):
    with open(PATH_TO_LOG_FILE, 'a') as f:
        f.write(f"{dt.now().strftime(DATETIME_FORMAT)} {module_name}: Exception {error_text}")

def log_user_request(module_name: str, request: str):
    with open(PATH_TO_LOG_FILE, 'a') as f:
        f.write(f"{dt.now().strftime(DATETIME_FORMAT)} {module_name}: User Request {request}")
