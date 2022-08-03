import os
import csv
from collections import OrderedDict

from model.constants import *


ASSIGNMENT_FILE_PATH = os.path.join("config", 'assignments.csv')
DEPARTMENT_FILE_PATH = os.path.join("config", 'departments.csv')
JOBS_FILE_PATH = os.path.join("config", 'jobs.csv')
WORKERS_FILE_PATH = os.path.join("config", 'workers.csv')

ASSIGNMENT_EDITED_FILE_PATH = os.path.join("config", 'assignments_edited.csv')
DEPARTMENT_EDITED_FILE_PATH = os.path.join("config", 'departments_edited.csv')
JOBS_EDITED_FILE_PATH = os.path.join("config", 'jobs_edited.csv')
WORKERS_EDITED_FILE_PATH = os.path.join("config", 'workers_edited.csv')

CSV_DELIMITERS = ";"
CSV_WORKER_FIELDNAMES = ID_FIELD, FIO_FIELD, PHONE_FIELD
CSV_DEPARTMENT_FIELDNAMES = ID_FIELD, DEPARTMENT_FIELD
CSV_JOB_FIELDNAMES = ID_FIELD, JOB_FIELD
CSV_ASSIGNMENT_FIELDNAMES = ID_WORKER_FIELD, ID_DEPARTMENT_FIELD, ID_JOB_FIELD


def get_department_id(department: str):
    if not os.path.isfile(DEPARTMENT_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    with open(DEPARTMENT_FILE_PATH, 'r', newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=CSV_DELIMITERS)
        for line in csv_reader:
            if line[DEPARTMENT_FIELD] == department:
                return line[ID_FIELD]
    return -1


def get_worker_id(worker: str):
    if not os.path.isfile(WORKERS_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    with open(WORKERS_FILE_PATH, 'r', newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=CSV_DELIMITERS)
        for line in csv_reader:
            if line[FIO_FIELD] == worker:
                return line[ID_FIELD]
    return -1


def get_job_id(job: str):
    if not os.path.isfile(JOBS_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    with open(JOBS_FILE_PATH, 'r', newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=CSV_DELIMITERS)
        for line in csv_reader:
            if line[JOB_FIELD] == job:
                return line[ID_FIELD]
    return -1


def get_next_available_worker_id() -> str:
    ids = []
    with open(WORKERS_FILE_PATH, 'r', newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=CSV_DELIMITERS)
        for line in csv_reader:
            ids.append(line[ID_FIELD])
    ids_int = list(map(int, ids))
    if max(ids_int) == len(ids_int):
        return str(len(ids) + 1)
    worker_id_list = sorted(set(range(1, max(ids_int) + 1)).difference(ids_int))
    return str(worker_id_list[0])


def show_all_workers() -> dict:
    if not os.path.isfile(WORKERS_FILE_PATH) or not os.path.isfile(JOBS_FILE_PATH) \
    or not os.path.isfile(DEPARTMENT_FILE_PATH) or not os.path.isfile(ASSIGNMENT_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    result_dict = {}
    with open(WORKERS_FILE_PATH, 'r', newline="") as f:
        csv_reader = csv.DictReader(f, delimiter=CSV_DELIMITERS)
        for line in csv_reader:
            result_dict[line[ID_FIELD]] = OrderedDict({ID_FIELD: line[ID_FIELD], FIO_FIELD: line[FIO_FIELD], PHONE_FIELD: line[PHONE_FIELD]})
    with open(ASSIGNMENT_FILE_PATH, 'r', newline="") as ass_file, open(JOBS_FILE_PATH, 'r', newline="") as jobs_file, open(DEPARTMENT_FILE_PATH, 'r', newline="") as dep_file:
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
    department_id = get_department_id(data[DEPARTMENT_FIELD])
    job_id = get_job_id(data[JOB_FIELD])
    if department_id == -1 or job_id == -1:
        raise ValueError(__name__, "No such department or job")
    worker_id = get_next_available_worker_id()
    if not os.path.isfile(WORKERS_FILE_PATH) or not os.path.isfile(ASSIGNMENT_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    with open(WORKERS_FILE_PATH, 'a') as worker_file, open(ASSIGNMENT_FILE_PATH, 'a', newline="") as ass_file:
        csv_writer = csv.DictWriter(worker_file, fieldnames=CSV_WORKER_FIELDNAMES, delimiter=CSV_DELIMITERS)
        csv_writer.writerow({ID_FIELD: worker_id, FIO_FIELD: data[FIO_FIELD], PHONE_FIELD: data[PHONE_FIELD]})
        
        csv_writer = csv.DictWriter(ass_file,fieldnames=CSV_ASSIGNMENT_FIELDNAMES, delimiter=CSV_DELIMITERS)
        csv_writer.writerow({ID_WORKER_FIELD: worker_id, ID_DEPARTMENT_FIELD: department_id, ID_JOB_FIELD: job_id})

    return {ID_FIELD: worker_id, FIO_FIELD: data[FIO_FIELD], PHONE_FIELD: data[PHONE_FIELD], 
            DEPARTMENT_FIELD: data[DEPARTMENT_FIELD], JOB_FIELD: data[JOB_FIELD]}


def remove_worker(worker_fio: str):
    worker_id = get_worker_id(worker_fio)
    if worker_id == -1:
        raise ValueError(__name__, "Worker does not exists")
    if not os.path.isfile(WORKERS_FILE_PATH) or not os.path.isfile(ASSIGNMENT_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    with open(WORKERS_FILE_PATH, 'r', newline="") as worker_file, open(ASSIGNMENT_FILE_PATH, 'r', newline='') as ass_file, \
         open(WORKERS_EDITED_FILE_PATH, 'w', newline='') as worker_edited_file, open(ASSIGNMENT_EDITED_FILE_PATH, 'w', newline='') as ass_edited_file:
        csv_reader = csv.DictReader(worker_file, delimiter=CSV_DELIMITERS)
        csv_writer = csv.DictWriter(worker_edited_file, fieldnames=CSV_WORKER_FIELDNAMES, delimiter=CSV_DELIMITERS)
        csv_writer.writeheader()
        for line in csv_reader:
            if line[ID_FIELD] != worker_id:
                csv_writer.writerow(line)
        csv_reader = csv.DictReader(ass_file, delimiter=CSV_DELIMITERS)
        csv_writer = csv.DictWriter(ass_edited_file, fieldnames=CSV_ASSIGNMENT_FIELDNAMES, delimiter=CSV_DELIMITERS)
        csv_writer.writeheader()
        for line in csv_reader:
            if line[ID_WORKER_FIELD] != worker_id:
                csv_writer.writerow(line)
    os.replace(WORKERS_EDITED_FILE_PATH, WORKERS_FILE_PATH)
    os.replace(ASSIGNMENT_EDITED_FILE_PATH, ASSIGNMENT_FILE_PATH)


def edit_worker(data: dict):
    raise NotImplementedError(__name__, "Not implemented")


def show_all_departments() -> dict:
    if not os.path.isfile(DEPARTMENT_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    result_dict = {}
    with open(DEPARTMENT_FILE_PATH, 'r', newline="") as csv_file:
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
    with open(JOBS_FILE_PATH, 'r', newline="") as csv_file:
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
