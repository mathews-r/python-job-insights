from src.pre_built.sorting import sort_by


def test_sort_by_criteria():
    assert sort_by('xablau', "max_salary")
