class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def rob_house(i, start):
            if (i, start) in dp:
                return dp[(i, start)]
            if i == len(nums) - 1 and start == True:
                return 0
            if i >= len(nums):
                return 0
            if i == 0:
                dp[(i, start)] = max(rob_house(i + 2, True) + nums[i], rob_house(i + 1, False))
            else:
                dp[(i, start)] = max(rob_house(i + 2, start) + nums[i], rob_house(i + 1, start))

            return dp[(i, start)] 
        return rob_house(0, False)
        