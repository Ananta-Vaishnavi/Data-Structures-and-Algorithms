class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            if target-nums[i] in hashmap:
                return [hashmap[(target-nums[i])],i]
        # here we add element in hash map only after iterating to it because we do not get a duplicated value where we add up the same element twice
        # consider [2,1,3,5,7] and target=4
        # here we do this stept to get 1,3 and not 2,2
            hashmap[nums[i]]=i
