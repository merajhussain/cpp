def max_profit(prices):
    if len(prices)==0:
        return 0
    maxprofit=0
    minimumbuyingprice=prices[0]
    for i in range (1,len(prices)):
        if prices[i]<minimumbuyingprice:
            minimumbuyingprice = prices[i]
        maxprofit = max(maxprofit,prices[i]-minimumbuyingprice)
    return maxprofit


