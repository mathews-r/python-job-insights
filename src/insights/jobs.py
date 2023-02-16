import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode="r", encoding="utf-8") as file:
        jobs = csv.DictReader(file, delimiter=",")
        job_list = []
        for job in jobs:
            job_list.append(job)

    return job_list


def get_unique_job_types(path: str) -> List[str]:

    jobs = read(path)

    type_jobs = []
    for job in jobs:
        item = job["job_type"]
        if item not in type_jobs:
            type_jobs.append(job["job_type"])
    return type_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
