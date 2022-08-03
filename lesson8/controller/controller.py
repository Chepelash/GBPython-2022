from logger import logger
from model import *


def show_all_workers():
    return manipulator.show_all_workers()


def add_new_worker():
    data = command_reader.get_new_worker_data()
    return manipulator.add_new_worker(data)


def remove_worker():
    data = command_reader.get_worker_to_remove()
    return manipulator.remove_worker(data)


def change_worker_data():
    data = command_reader.get_edited_worker_data()
    return manipulator.edit_worker(data)


def show_all_departments():
    return  manipulator.show_all_departments()


def add_new_department():
    data = command_reader.get_new_department_data()
    return  manipulator.add_new_department(data)


def remove_department():
    data = command_reader.get_department_to_remove()
    return  manipulator.remove_department(data)


def change_department_data():
    data = command_reader.get_edited_department_data()
    return  manipulator.edit_department(data)


def show_all_jobs():
    return  manipulator.show_all_jobs()


def add_new_job():
    data = command_reader.get_new_job_data()
    return  manipulator.add_new_job(data)


def remove_job():
    data = command_reader.get_job_to_remove()
    return  manipulator.remove_job(data)


def change_job_data():
    data = command_reader.get_edited_job_data()
    return  manipulator.edit_job(data)


def import_table():
    data = command_reader.get_import_data()
    return  manipulator.import_table(data)


def export_table():
    data = command_reader.get_export_data()
    return  manipulator.export_table(data)