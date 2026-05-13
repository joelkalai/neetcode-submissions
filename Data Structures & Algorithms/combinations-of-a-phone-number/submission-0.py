class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [] 
        tmp = []
        possible = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def dfs(digit, i):
            if digit >= len(digits):
                res.append(''.join(tmp))
                return
            if i >= len(possible[int(digits[digit]) - 2]):
                return 
            curr = possible[int(digits[digit]) - 2]
            tmp.append(curr[i])
            dfs(digit + 1, 0)
            tmp.pop()
            dfs(digit, i + 1)
        dfs(0, 0)
        return res

            