class Solution:
    def groupThePeople(self, groupSizes):
        result = []
        groups = []

        for size in range(max(groupSizes) + 1):
            groups.append([])

        for i, size in enumerate(groupSizes):
            groups[size].append(i)
            if len(groups[size]) == size:
                result.append(groups[size])
                groups[size] = []

        return result

groupSizes = []
solution = Solution()
