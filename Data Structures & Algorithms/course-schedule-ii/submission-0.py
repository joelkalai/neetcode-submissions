class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        added = set()
        preMap = {p : [] for p in range(numCourses)}
        for p, x in prerequisites:
            preMap[p].append(x)
        def dfs(p):
            if p in visited:
                return False 
            
            if preMap[p] == []:
                if p not in added:
                    res.append(p) # first course to take 
                    added.add(p) # cfm can pre
                return True
            visited.add(p)
            for i in preMap[p]:
                x = dfs(i)
                if not x:
                    return False
            visited.remove(p)
            preMap[p] = [] 
            if p not in added:
                added.add(p)
                res.append(p)
            return True 
        for i in range(numCourses):
            x = dfs(i)
            if not x:
                return []

        return res
            
            