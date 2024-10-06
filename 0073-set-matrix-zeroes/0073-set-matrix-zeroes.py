class Solution:
    def setZeroes(self, matrix): 

        if not matrix or not matrix[0]:
           return "Matrix is empty"

        n=[0]*len(matrix) #row
        m=[0]*len(matrix[0]) #column
        #row 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    n[i] = 1  # i번째 행에 0이 있음을 기록
                    m[j] = 1  # j번째 열에 0이 있음을 기록

        # 2단계: 0이 있는 행과 열을 0으로 설정
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if n[i] == 1 or m[j] == 1:  # 행 또는 열에 0이 있으면
                    matrix[i][j] = 0  # 해당 요소를 0으로 설정

        return matrix

matrix=[]
a=Solution()
print(a.setZeroes(matrix))