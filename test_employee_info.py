import employee_info as EMPINFO
from employee_info import employee_data as EMPDATA


def test_get_employees_by_age_range_method1():
    result = []
    expected = [EMPDATA[0], EMPDATA[4]]
    result = EMPINFO.get_employees_by_age_range(26, 33)
    assert (result == expected)


def test_get_employees_by_age_range_method2():
    result = []
    expected = [EMPDATA[x] for x in [0,1,3,4]]  # Compare this approach with previous test.
    result = EMPINFO.get_employees_by_age_range(24, 39)
    assert (result == expected)


def test_calculate_average_salary():
    expected = 60166.67
    result = EMPINFO.calculate_average_salary()
    result = round(result,2)
    assert (result == expected)    



def test_get_employees_by_dept():
    result = []
    expected = [EMPDATA[3], EMPDATA[4]]
    result = EMPINFO.get_employees_by_dept('Engineering')
    assert (result == expected)    


