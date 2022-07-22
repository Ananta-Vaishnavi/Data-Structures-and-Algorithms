class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        maximum=0
        start=0
        end=k-1
        answer=[]
        while(end<n):
            if maximum==0:
                maximum=max(arr[start:start+k])
            else:
                if arr[start-1]==maximum:
                    maximum=max(arr[start:start+k])
                else:
                    maximum=max(maximum,arr[end])
            answer.append(maximum)
            start+=1   
            end+=1
        return answer
