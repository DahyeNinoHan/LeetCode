class Solution:
    def groupThePeople(self,groupSizes):
        size_to_people = {}
        
        # Step 2: Populate the dictionary
        for person, size in enumerate(groupSizes):
            if size not in size_to_people:
                size_to_people[size] = []
            size_to_people[size].append(person)
        
        result = []
        
        # Step 3: Form groups
        for size, people in size_to_people.items():
            for i in range(0, len(people), size):
                result.append(people[i:i + size])
        
        return result




groupSizes=[]

solution = Solution()
solution.groupThePeople(groupSizes)