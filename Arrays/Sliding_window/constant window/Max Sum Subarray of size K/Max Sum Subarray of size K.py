class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        sum=0
        for i in range(K):
            sum+=Arr[i]
        max=sum
        for i in range(N-K):
            sum-=Arr[i]
            sum+=Arr[i+K]
            if max<sum:
                max=sum
        return max
