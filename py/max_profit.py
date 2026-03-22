def max_profit(prices):
    if len(prices)==0:
        return 0
    mp=0
    mbp=prices[0]
    for i in range (1,len(prices)):
        if prices[i]<mbp:
            mbp = prices[i]
        mp = max(mp,prices[i]-mbp)
    return mp


