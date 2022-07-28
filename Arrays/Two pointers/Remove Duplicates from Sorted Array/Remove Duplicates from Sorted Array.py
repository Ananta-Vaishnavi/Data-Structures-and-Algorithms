class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start,end=0,1
        while end<len(nums):
            if nums[start]==nums[end]:
                nums.pop(end)
            else:
                start+=1
                end+=1
        return end+1
