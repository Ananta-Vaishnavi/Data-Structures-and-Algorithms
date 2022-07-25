# Works only for positive values.
class Solution:
    def lenOfLongSubarr (self, A, N, target) : 
        #Complete the function
        max_len=0
        c_sum=0
        right =0
        left=0
        max_len=0
        while right<N:
            c_sum+=A[right]
            while c_sum>target:
                c_sum-=A[left]
                left+=1
            if c_sum==target:
                max_len=max(max_len,right-left+1)
            right+=1
        return max_len
