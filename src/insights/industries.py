import src.insights.jobs as jobs
from typing import List, Dict


def get_unique_industries(path: str) -> List[str]:
    industries = jobs.read(path)

    type_industries = []
    for industry in industries:
        item = industry["industry"]
        if item not in type_industries:
            type_industries.append(industry["industry"])
    return type_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
