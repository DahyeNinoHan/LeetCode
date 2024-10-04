class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix=[]
        # Create a numRow*numRow matrix filled with 0
        # matrix = [[0]*(i+1)] for i in range(numrows)
        for i in range(numRows):
            row = [0]*(i+1) # 각 행을 0으로 초기화,  길이는 i+1
            matrix.append(row) # 생성한 행을 matrix에 추가

        # Make 1 on all elements in first column
        # Make 1 on matrix[i][i] 
        for i in range(numRows):
            matrix[i][0]=1
            matrix[i][i]=1

        # (i-1, j-1) + (i-1, j) = (i,j)
        for i in range (2,numRows):
            for j in range (1, i):
                matrix[i][j]=matrix[i-1][j-1]+matrix[i-1][j]
        return matrix
            
a=Solution()
numRows=5
a.generate(numRows)
