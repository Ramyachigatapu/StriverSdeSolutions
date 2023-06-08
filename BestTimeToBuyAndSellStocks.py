

def maximumProfit(prices):
    maxProfit = 0
    minPrice = float('inf')
    for i in range(len(prices)):
        minPrice = min(minPrice, prices[i])
        maxProfit = max(maxProfit, prices[i] - minPrice)
    return maxProfit
    # Write your code here.
