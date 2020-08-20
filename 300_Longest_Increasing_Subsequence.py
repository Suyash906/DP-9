class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:return 0
        max_len = 1
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_len = max(max_len, dp[i])
        return max_len