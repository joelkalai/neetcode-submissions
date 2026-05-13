class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        res = []
        tmp = set()
        j = 0
        for i in range(len(s)):
            count[s[i]] -= 1
            tmp.add(s[i])
            can = True
            for c in tmp:
                if count[c] != 0:
                    can = False
                    break 
            if can:
                res.append(i - j + 1)
                j = i + 1
        return res


