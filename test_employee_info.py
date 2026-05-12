import employee_info as ei

def test_get_employees_by_age_range():
    result = ei.get_employees_by_age_range(30, 40) #30 and 40 are not included in the result
    assert (len(result) == 2)
    assert (result[0]["name"] == "Chloe"  )

def test_calculate_average_salary():
    result = ei.calculate_average_salary()
    assert (result == 60166.67)    

def test_get_employees_by_dept():
    result = ei.get_employees_by_dept("Sales")
    assert (len(result) == 2)
    assert (result[0] == "John"  )