import os


ASSIGNMENT_FILE_PATH = os.path.join("config", 'assignments.csv')
DEPARTMENT_FILE_PATH = os.path.join("config", 'departments.csv')
JOBS_FILE_PATH = os.path.join("config", 'jobs.csv')
WORKERS_FILE_PATH = os.path.join("config", 'workers.csv')


def is_file_exists(fpath: str) -> bool:
    """checks if file still there"""
    return os.path.isfile(fpath)


def show_all_workers():
    raise NotImplementedError(__name__, "Not implemented")


def add_new_worker(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def remove_worker(worker_id: str):
    raise NotImplementedError(__name__, "Not implemented")


def edit_worker(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def show_all_departments():
    raise NotImplementedError(__name__, "Not implemented")


def add_new_department(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def remove_department(department_id: str):
    raise NotImplementedError(__name__, "Not implemented")


def edit_department(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def show_all_jobs():
    raise NotImplementedError(__name__, "Not implemented")


def add_new_job(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def remove_job(job_id: str):
    raise NotImplementedError(__name__, "Not implemented")


def edit_job(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def validate_tables(data: tuple) -> bool:
    raise NotImplementedError(__name__, "Not implemented")


def import_table(data: tuple) -> bool:
    raise NotImplementedError(__name__, "Not implemented")


def export_table(data: str) -> tuple:
    raise NotImplementedError(__name__, "Not implemented")
