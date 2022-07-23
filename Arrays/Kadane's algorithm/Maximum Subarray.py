#https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        max_sum=nums[0]
        for i in range(len(nums)):
            current_sum=max(current_sum+nums[i],nums[i])
            max_sum=max(max_sum,current_sum)
        return max_sum
