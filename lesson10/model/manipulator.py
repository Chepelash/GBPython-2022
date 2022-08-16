import os
import shutil
import csv
from collections import OrderedDict

from constants import *

ASSIGNMENT_FILE_PATH = os.path.join("config", 'assignments.csv')
DEPARTMENT_FILE_PATH = os.path.join("config", 'departments.csv')
JOBS_FILE_PATH = os.path.join("config", 'jobs.csv')
WORKERS_FILE_PATH = os.path.join("config", 'workers.csv')

CSV_DELIMITERS = ";"
CSV_WORKER_FIELDNAMES = ID_FIELD, FIO_FIELD, PHONE_FIELD
CSV_DEPARTMENT_FIELDNAMES = ID_FIELD, DEPARTMENT_FIELD
CSV_JOB_FIELDNAMES = ID_FIELD, JOB_FIELD
CSV_ASSIGNMENT_FIELDNAMES = ID_WORKER_FIELD, ID_DEPARTMENT_FIELD, ID_JOB_FIELD


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

def show_all_departments() -> dict:
    if not os.path.isfile(DEPARTMENT_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    result_dict = {}
    with open(DEPARTMENT_FILE_PATH, 'r', newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=CSV_DELIMITERS)
        for line in csv_reader:
            result_dict[line[ID_FIELD]] = OrderedDict({ID_FIELD: line[ID_FIELD], DEPARTMENT_FIELD: line[DEPARTMENT_FIELD]})
    return result_dict

def show_all_jobs():
    if not os.path.isfile(JOBS_FILE_PATH):
        raise FileNotFoundError(__name__, "BD files not found")
    result_dict = {}
    with open(JOBS_FILE_PATH, 'r', newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=CSV_DELIMITERS)
        for line in csv_reader:
            result_dict[line[ID_FIELD]] = OrderedDict({ID_FIELD: line[ID_FIELD], JOB_FIELD: line[JOB_FIELD]})
    return result_dict