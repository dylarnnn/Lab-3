import price_info as pi



def test_total_cost_shopping():
    totalCost = pi.total_cost_shopping()
    assert ( totalCost == 46.75)

def test_cost_of_fruit():
    totalFruitCost = pi.cost_of_fruits('apple', 10)
    assert ( totalFruitCost == 12 )