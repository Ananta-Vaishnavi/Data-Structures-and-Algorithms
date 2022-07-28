class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        i=0
        j=len(num)-1
        while i<j:
            if num[i]+num[j]>target:
                j=j-1
            elif num[i]+num[j]<target:
                i=i+1
            else:
                return [i+1,j+1]
