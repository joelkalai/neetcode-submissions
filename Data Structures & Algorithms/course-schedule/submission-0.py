class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {p: [] for p in range(numCourses)}
        for p, x in prerequisites:
            preMap[p].append(x)
        
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            if preMap[i] == []:
                return True 
            visited.add(i)
            for x in preMap[i]:
                curr = dfs(x)
                if not curr:
                    return False
            visited.remove(i)
            preMap[i] = []
            return True 
        for i in range(numCourses):
            x = dfs(i)
            if not x:
                return False
        return True





         