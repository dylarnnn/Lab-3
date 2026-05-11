import Lab2.bmi as bmi


def test_FRIDGEHOARDEROVERWEIGHT():
    result = bmi.calculate_bmi(1.73, 110)
    assert (result == 1)

def test_youresafefornow():
    result = bmi.calculate_bmi(1.73, 57)
    assert (result == 0)

def test_youreBONES():
    result = bmi.calculate_bmi(1.73, 40)
    assert (result == -.1)