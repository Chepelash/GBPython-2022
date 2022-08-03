import os
import csv
from collections import OrderedDict


ASSIGNMENT_FILE_PATH = os.path.join("config", 'assignments.csv')
DEPARTMENT_FILE_PATH = os.path.join("config", 'departments.csv')
JOBS_FILE_PATH = os.path.join("config", 'jobs.csv')
WORKERS_FILE_PATH = os.path.join("config", 'workers.csv')

CSV_DELIMITERS = ";"
ID_FIELD = "id"
FIO_FIELD = "fio"
PHONE_FIELD = "phone"
DEPARTMENT_FIELD = "department"
JOB_FIELD = "job"
ID_WORKER_FIELD = "id_worker"
ID_JOB_FIELD = "id_job"
ID_DEPARTMENT_FIELD = "id_department"


def show_all_workers() -> dict:
    if not os.path.isfile(WORKERS_FILE_PATH) or not os.path.isfile(JOBS_FILE_PATH) \
    or not os.path.isfile(DEPARTMENT_FILE_PATH) or not os.path.isfile(ASSIGNMENT_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    result_dict = {}
    with open(WORKERS_FILE_PATH, 'r') as f:
        csv_reader = csv.DictReader(f, delimiter=CSV_DELIMITERS)
        for line in csv_reader:
            result_dict[line[ID_FIELD]] = OrderedDict({ID_FIELD: line[ID_FIELD], FIO_FIELD: line[FIO_FIELD], PHONE_FIELD: line[PHONE_FIELD]})
    with open(ASSIGNMENT_FILE_PATH, 'r') as ass_file, open(JOBS_FILE_PATH, 'r') as jobs_file, open(DEPARTMENT_FILE_PATH, 'r') as dep_file:
        ass_reader = csv.DictReader(ass_file, delimiter=CSV_DELIMITERS)
        jobs_reader = csv.DictReader(jobs_file, delimiter=CSV_DELIMITERS)
        dep_reader = csv.DictReader(dep_file, delimiter=CSV_DELIMITERS)
        for line in ass_reader:
            id_worker = line[ID_WORKER_FIELD]
            id_job = line[ID_JOB_FIELD]
            id_department = line[ID_DEPARTMENT_FIELD]
            jobs_file.seek(0)
            dep_file.seek(0)
            for line in jobs_reader:
                if line[ID_FIELD] == id_job:
                    result_dict[id_worker][JOB_FIELD] = line[JOB_FIELD]                   
                    break
            for line in dep_reader:
                if line[ID_FIELD] == id_department:
                    result_dict[id_worker][DEPARTMENT_FIELD] = line[DEPARTMENT_FIELD]
                    break
    return result_dict    


def add_new_worker(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def remove_worker(worker_id: str):
    raise NotImplementedError(__name__, "Not implemented")


def edit_worker(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def show_all_departments() -> dict:
    if not os.path.isfile(DEPARTMENT_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    result_dict = {}
    with open(DEPARTMENT_FILE_PATH, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=CSV_DELIMITERS)
        for line in csv_reader:
            result_dict[line[ID_FIELD]] = OrderedDict({ID_FIELD: line[ID_FIELD], DEPARTMENT_FIELD: line[DEPARTMENT_FIELD]})
    return result_dict


def add_new_department(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def remove_department(department_id: str):
    raise NotImplementedError(__name__, "Not implemented")


def edit_department(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def show_all_jobs():
    if not os.path.isfile(JOBS_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    result_dict = {}
    with open(JOBS_FILE_PATH, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=CSV_DELIMITERS)
        for line in csv_reader:
            result_dict[line[ID_FIELD]] = OrderedDict({ID_FIELD: line[ID_FIELD], JOB_FIELD: line[JOB_FIELD]})
    return result_dict


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
