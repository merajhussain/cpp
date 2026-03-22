from max_profit import max_profit


def test1_max_profit():
    prices = [7, 1, 5, 3, 6, 4]
    expectedprofit = 5
    assert expectedprofit == max_profit(prices)


def test2_max_profit():
    prices = [7, 6, 4, 3, 1]
    expectedprofit = 0
    assert expectedprofit == max_profit(prices)

def test3_max_profit():
    prices = [1, 2, 3, 4, 5]
    expectedprofit = 4
    assert expectedprofit == max_profit(prices)

def test4_max_profit():
    prices = [5]
    expectedprofit = 0
    assert expectedprofit == max_profit(prices)

def test5_max_profit():
    prices = [3,3,3,3]
    expectedprofit = 0
    assert expectedprofit == max_profit(prices)

def test6_max_profit():
    prices = [2,1,2,1,0,1,2]
    expectedprofit = 2
    assert expectedprofit == max_profit(prices)

def test7_max_profit():
    prices = [1,10,2,9]
    expectedprofit = 9
    assert expectedprofit == max_profit(prices)

def test8_max_profit():
    prices = [10, 1, 5, 6]
    expectedprofit = 5
    assert expectedprofit == max_profit(prices)

def test9_max_profit():
    prices = [2, 4, 1]
    expectedprofit = 2
    assert expectedprofit == max_profit(prices)

def test10_max_profit():
    prices = [1,2]
    expectedprofit = 1
    assert expectedprofit == max_profit(prices)
