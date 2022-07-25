#User function Template for python3

class Solution:
    def longestKSubstr(self,s, k):
        right=0
        left=0
        counter={}
        max_len=-1
        while right<len(s):
            if s[right] in counter:
                counter[s[right]]+=1
            else:
                counter[s[right]]=1
            if len(counter)>k:
                while len(counter)>k :
                    if counter[s[left]]==1:
                        counter.pop(s[left])     
                    else:
                        counter[s[left]]-=1
                    left+=1
            elif len(counter)==k:
                max_len=max(max_len,right-left+1)
                while len(counter)==k and right>len(s) :
                    if len(counter)==k:
                        max_len=max(max_len,right-left+1)
                        right+=1
                    if s[right] in counter:
                        counter[s[right]]+=1
                    else:
                        counter[s[right]]=1
            right+=1
        return max_len
