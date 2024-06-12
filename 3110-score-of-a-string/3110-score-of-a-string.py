class Solution(object):
    def scoreOfString(self, s):
        lst = []
        for i in range(len(s)):
            lst.append(ord(s[i]))
        diff = []
        for j in range(len(s)-1):
            diff.append(abs(lst[j+1] - lst[j]))
        
        print(diff)

        return(sum(diff))
        
s=''

cal = Solution()
cal.scoreOfString(s)