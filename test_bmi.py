import Lab2_2620p.bmi as bmi


def test_bmi_normal_weight():
    expected = 0
    result = bmi.calculate_bmi(weight = 60.0, height = 1.80)
    assert (result == expected)


def test_bmi_over_weight():
    expected = 1
    result = bmi.calculate_bmi(weight = 90.0, height = 1.80)
    assert (result == expected)


def test_bmi_under_weight():
    expected = -1
    result = bmi.calculate_bmi(weight = 50.0, height = 1.80)
    assert (result == expected)

