# Time complexity O(n): 
# Memory O(1)
# Runtime: Beats 76.73% | Memory: Beats 94.02%

def maxProfit(prices: list[int]) -> int:
    buy = prices[0]
    sell = prices[0]
    low = prices[0] # [index, value]

    for i in prices:
        if i <= low:
            low = i

        if (i - low) > (sell - buy):
            buy = low
            sell = i

    return sell - buy

# prices = [3,3,5,0,0,3,1,4]
prices = [7,1,5,3,6,4]
print(maxProfit(prices))

# ------------------- SIMILAR APPROACHES ----------------- #

# Time complexity O(n): 
# Memory O(1)
# Runtime: Beats 48.56% | Memory: Beats 23.08%
def maxProfit(prices: list[int]) -> int:
    buy = prices[0]
    profit = 0

    for i in prices:
        cost = i - buy
        profit = max(profit, cost)
        buy = min(i, buy)

    return profit

# prices = [3,3,5,0,0,3,1,4]
# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))
