class Solution:
    def setZeroes(self, matrix): 

        if not matrix or not matrix[0]:
           return "Matrix is empty"

        n=[0]*len(matrix) #row
        m=[0]*len(matrix[0]) #column
        #row 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    n[i]=1
                    m[j]=1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if n[i]==1 or m[j]==1:
                    matrix[i][j]=0

        return matrix

matrix=[]
a=Solution()
print(a.setZeroes(matrix))