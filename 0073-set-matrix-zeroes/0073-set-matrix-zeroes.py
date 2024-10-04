class Solution:
    def setZeroes(self, matrix):  # n과 m을 제거
        n = len(matrix)  # 행의 개수
        m = len(matrix[0])  # 열의 개수
        row = [0] * n  # row array
        col = [0] * m  # col array

        # Traverse the matrix:
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # mark ith index of row with 1:
                    row[i] = 1
                    # mark jth index of col with 1:
                    col[j] = 1

        # Finally, mark all (i, j) as 0
        # if row[i] or col[j] is marked with 1.
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0

        return matrix


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

    # Solution 클래스의 인스턴스를 생성하고 setZeroes 메서드 호출
    solution = Solution()
    ans = solution.setZeroes(matrix)

    print(matrix)
