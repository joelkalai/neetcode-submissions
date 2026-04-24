class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create a sliding window 
        # for each window take longest same string and the number of not same <= k 
        # iterating through with a subset, such that all characters are the same
        # if not same shift pointer leftwards 
        # key here is to find the most frequent character in the window, replace every other character
        # can use heap? 
        # at any point in time your window should have 1 dominant character
        # every other character can just be replaced if they are <= k 
        window = defaultdict(int)
        l = 0
        maxf = 0 
        res = 0
        for r in range(len(s)):
            window[s[r]] += 1
            maxf = max(window[s[r]], maxf)
            while r- l + 1 - maxf > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res