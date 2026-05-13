class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c : i for i, c in enumerate(s)}
        res = [] 
        start = end = 0 
        for j in range(len(s)):
            end = max(last[s[j]], end)
            if end == j:
                res.append(end - start + 1)
                start = j + 1
        return res