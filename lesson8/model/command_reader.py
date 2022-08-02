from logger import logger


def get_new_worker_data() -> dict:
    """Get filling data"""
    raise NotImplementedError(__name__, "Not implemented")

def get_worker_to_remove() -> str:
    """Get worker id"""
    raise NotImplementedError(__name__, "Not implemented")

def get_edited_worker_data() -> dict:
    raise NotImplementedError(__name__, "Not implemented")

def get_new_department_data() -> dict:
    """Get filling data"""
    raise NotImplementedError(__name__, "Not implemented")

def get_department_to_remove() -> str:
    """Get department id"""
    raise NotImplementedError(__name__, "Not implemented")

def get_edited_department_data() -> dict:
    raise NotImplementedError(__name__, "Not implemented")

def get_new_job_data() -> dict:
    """Get filling data"""
    raise NotImplementedError(__name__, "Not implemented")

def get_job_to_remove() -> str:
    """Get job id"""
    raise NotImplementedError(__name__, "Not implemented")

def get_edited_job_data() -> dict:
    raise NotImplementedError(__name__, "Not implemented")

def get_import_data() -> tuple:
    """Get paths to csv files"""
    raise NotImplementedError(__name__, "Not implemented")

def get_export_data() -> str:
    """Get dir to write csv files"""
    raise NotImplementedError(__name__, "Not implemented")
