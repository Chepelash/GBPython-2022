from logger import logger
from model.constants import *

def get_new_worker_data() -> dict:
    """Get filling data"""

    fio = input("Введите имя работника > ")
    phone_number = input("Введите телефон работника > ")
    department = input("Введите департамент работника > ")
    job = input("Введите должность работника > ")
    return {FIO_FIELD: fio, PHONE_FIELD: phone_number, DEPARTMENT_FIELD: department, JOB_FIELD: job}    

def get_worker_to_remove() -> str:
    """Get worker id"""
    data = input("Введите ФИО работника > ")
    return data    

def get_edited_worker_data() -> dict:
    raise NotImplementedError(__name__, "Not implemented")

def get_new_department_data() -> dict:
    """Get filling data"""
    new_dep_name = input("Введите название нового отдела > ")
    return new_dep_name

def get_department_to_remove() -> str:
    """Get department id"""
    data = input("Введите название департамента > ")
    return data
    

def get_edited_department_data() -> dict:
    old_dep_name = input("Введите старое название отдела > ")
    new_dep_name = input("Введите новое название отдела > ")
    return {OLD_VALUE: old_dep_name, NEW_VALUE: new_dep_name}

def get_new_job_data() -> str:
    """Get filling data"""
    new_job_name = input("Введите название новой должности > ")
    return new_job_name

def get_job_to_remove() -> str:
    """Get job id"""
    data = input("Введите название должности > ")
    return data
    

def get_edited_job_data() -> dict:
    old_job_name = input("Введите старое название профессии > ")
    new_job_name = input("Введите новое название профессии > ")
    return {OLD_VALUE: old_job_name, NEW_VALUE: new_job_name}

def get_import_data() -> dict:
    """Get paths to csv files"""
    data = {}
    data[VALIDATE_ASS_KEY] = input("Введите путь к файлу назначений > ")
    data[VALIDATE_DEP_KEY] = input("Введите путь к файлу отделов > ")
    data[VALIDATE_JOB_KEY] = input("Введите путь к файлу должностей > ")
    data[VALIDATE_WORK_KEY] = input("Введите путь к файлу работников > ")
    return data
    

def get_export_data() -> str:
    """Get dir to write csv files"""
    data = input("Введите папку для экспорта")
    return data
