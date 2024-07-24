class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result=0

        for i in accounts:
            total = sum(i)
            if result < total:
                result = total

        return result
        
accounts=[[1,2,3],[3,2,1]]
a = Solution()
a.maximumWealth(accounts)
