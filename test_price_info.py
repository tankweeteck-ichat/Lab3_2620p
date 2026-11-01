import price_info as PRICEINFO

def test_total_cost_shopping():
    expected = 46.75
    result = PRICEINFO.total_cost_shopping()
    assert (result == expected)



def test_cost_of_fruits():
    expected = 32.5
    result = PRICEINFO.cost_of_fruits('watermelon', 5)
    assert (result == expected)



