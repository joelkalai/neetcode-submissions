class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def rob_house(i):
            if i in dp:
                return dp[i]
            if i >= len(nums):
                return 0
            dp[i] = max(rob_house(i + 1), nums[i] + rob_house(i + 2))
            return dp[i]
        return rob_house(0)
        