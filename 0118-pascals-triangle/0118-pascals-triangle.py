class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix=[]
        for i in range(numRows):
            row=[0]*(i+1)
            matrix.append(row)
        for i in range(numRows):
            matrix[i][0]=1
            matrix[i][i]=1
        for i in range (2,numRows):
            for j in range (1, i):
                matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j]

        return matrix

numRows=5
a=Solution()
print(a.generate(numRows))





numRows=0
a=Solution()
print(a.generate(numRows))