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
    job_filtred = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_filtred.append(job)

    return job_filtred
