from src.pre_built.sorting import sort_by


def test_sort_by_criteria():

    mock_general = [
        {"min_salary": 20, "max_salary": 40, "date_posted": "2023-02-17"},
        {"min_salary": 10, "max_salary": 50, "date_posted": "2000-02-17"},
    ]

    mock_min_salary = [
        {"min_salary": 10, "max_salary": 50, "date_posted": "2000-02-17"},
        {"min_salary": 20, "max_salary": 40, "date_posted": "2023-02-17"},
    ]

    mock_max_salary = [
        {"min_salary": 10, "max_salary": 50, "date_posted": "2000-02-17"},
        {"min_salary": 20, "max_salary": 40, "date_posted": "2023-02-17"},
    ]

    mock_date_posted = [
        {"min_salary": 20, "max_salary": 40, "date_posted": "2023-02-17"},
        {"min_salary": 10, "max_salary": 50, "date_posted": "2000-02-17"},
    ]

    sort_by(mock_general, "min_salary")
    assert mock_general == mock_min_salary

    sort_by(mock_general, "max_salary")
    assert mock_general == mock_max_salary

    sort_by(mock_general, "date_posted")
    assert mock_general == mock_date_posted
