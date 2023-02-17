from typing import Union, List, Dict

from src.insights.jobs import read

# from jobs import read


def get_max_salary(path: str) -> int:
    salaries = read(path)

    max_salary = 0
    for salary in salaries:
        if salary["max_salary"] == "":
            max_salary = max_salary
        elif (
            salary["max_salary"] != "invalid"
            and int(salary["max_salary"]) > max_salary
        ):
            max_salary = int(salary["max_salary"])
    return max_salary


def get_min_salary(path: str) -> int:
    salaries = read(path)

    min_salary = get_max_salary("data/jobs.csv")
    for salary in salaries:
        if salary["min_salary"] == "":
            min_salary = min_salary
        elif (
            salary["min_salary"] != "invalid"
            and int(salary["min_salary"]) < min_salary
        ):
            min_salary = int(salary["min_salary"])
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    elif (
        isinstance(job["min_salary"], int) is False
        or isinstance(job["max_salary"], int) is False
    ):
        raise ValueError

    elif job["min_salary"] > job["max_salary"]:
        raise ValueError

    elif isinstance(salary, int) is False and isinstance(salary, str) is False:
        raise ValueError

    return int(salary) >= int(job["min_salary"]) and int(salary) <= int(
        job["max_salary"]
    )


print(matches_salary_range({"min_salary": 50, "max_salary": 100}, 60))


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    salary_filtred = []
    for item in jobs:
        if item["max_salary"] == salary or item["min_salary"]:
            salary_filtred.append(item)

    return salary_filtred
