class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = set()
        for t in triplets:
            Good = True 
            for i in range(len(t)):
                if target[i] < t[i]:
                    Good = False
                    break 
            if Good: 
                for i, j in enumerate(t):
                    if target[i] == j:
                        res.add(i)
            if len(res) == 3:
                return True
        return False
        