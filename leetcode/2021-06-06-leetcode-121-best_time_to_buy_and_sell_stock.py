from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        sell=prices[0]
        for idx in range(1,len(prices)):
            max_profit=max(max_profit, prices[idx]-sell)
            sell=min(sell,prices[idx])
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(prices))
    
    prices = [7, 6, 4, 3, 1]
    print(s.maxProfit(prices))
