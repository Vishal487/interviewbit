def maxProfit(p):
    prices = [0]
    for e in p:
        prices.append(e)
    dp = [0]*len(prices)
    dp[0] = 0
    dp[1] = prices[1]

    for i in range(2, len(dp)):
        dp[i] = prices[i]
        
        li = 1
        ri = i-1
        while li <= ri:
            if dp[li]+dp[ri] > dp[i]:
                dp[i] = dp[li] + dp[ri]
            li += 1
            ri -= 1
    
    return dp[-1]


p = [3,5,8,9,10,17,17,20]
print(maxProfit(p))

