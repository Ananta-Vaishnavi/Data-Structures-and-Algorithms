class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right=0
        left=0
        max_len=0
        counter={}
        while right<len(s):
            if s[right] in counter:
                counter[s[right]]+=1
            else:
                counter[s[right]]=1
            if len(counter)<right-left+1:
                if counter[s[left]]>1:
                    counter[s[left]]-=1
                else:
                    counter.pop(s[left])
                left+=1
            if len(counter)==right-left+1:
                max_len=max(max_len,right-left+1)
            right+=1
        return max_len
            
        
