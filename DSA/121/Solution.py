class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lower = prices[0]
        res = 0
        for n in prices :
            if lower > n:
                lower = n
            res = max(res,n-lower)
        return res