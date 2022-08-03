import os
import csv
from collections import OrderedDict


ASSIGNMENT_FILE_PATH = os.path.join("config", 'assignments.csv')
DEPARTMENT_FILE_PATH = os.path.join("config", 'departments.csv')
JOBS_FILE_PATH = os.path.join("config", 'jobs.csv')
WORKERS_FILE_PATH = os.path.join("config", 'workers.csv')


def is_file_exists(fpath: str) -> bool:
    """checks if file still there"""
    return os.path.isfile(fpath)


def show_all_workers() -> dict:
    if not os.path.isfile(WORKERS_FILE_PATH) or not os.path.isfile(JOBS_FILE_PATH) \
    or not os.path.isfile(DEPARTMENT_FILE_PATH) or not os.path.isfile(ASSIGNMENT_FILE_PATH):
        print(os.path.abspath('.'))
        raise FileNotFoundError(__name__, "BD files not found")
    result_dict = {}
    with open(WORKERS_FILE_PATH, 'r') as f:
        csv_reader = csv.DictReader(f, delimiter=";")
        for line in csv_reader:
            result_dict[line["id"]] = OrderedDict({"id": line["id"], "fio": line["fio"], "phone": line["phone"]})
    with open(ASSIGNMENT_FILE_PATH, 'r') as ass_file, open(JOBS_FILE_PATH, 'r') as jobs_file, open(DEPARTMENT_FILE_PATH, 'r') as dep_file:
        ass_reader = csv.DictReader(ass_file, delimiter=";")
        jobs_reader = csv.DictReader(jobs_file, delimiter=";")
        dep_reader = csv.DictReader(dep_file, delimiter=";")
        for line in ass_reader:
            id_worker = line["id_worker"]
            id_job = line["id_job"]
            id_department = line["id_department"]
            jobs_file.seek(0)
            dep_file.seek(0)
            for line in jobs_reader:
                if line["id"] == id_job:
                    result_dict[id_worker]["job"] = line["job"]                   
                    break
            for line in dep_reader:
                if line["id"] == id_department:
                    result_dict[id_worker]["department"] = line["department"]
                    break
    return result_dict    


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
