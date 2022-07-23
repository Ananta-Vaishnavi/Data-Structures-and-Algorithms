#    https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=len(nums)+1
        c_sum=0
        left=0
        for right in range(len(nums)):
            c_sum+=nums[right]
            while c_sum>=target:
                min_length=min(min_length,right-left+1)
                c_sum-=nums[left]
                left+=1    
        if min_length==len(nums)+1:
            return 0
        return min_length
