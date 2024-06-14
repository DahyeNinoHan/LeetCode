class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        return num + 2*t

num=0
t=0

a=Solution()
result = a.theMaximumAchievableX(num,t)
print(result)