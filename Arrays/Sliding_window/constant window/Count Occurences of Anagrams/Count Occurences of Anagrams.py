#User function Template for python3
from collections import Counter
class Solution:

	
	def search(self,pat, txt):
        answer=0
        original_count=dict(Counter(pat))
        count_track={}
        for i in range(len(pat)):
            if txt[i] in count_track:
                count_track[txt[i]]+=1 
            else:
                count_track[txt[i]]=1
        if original_count==count_track:
            answer+=1
        start=1
        end=len(pat)
        while end<len(txt):
            
            if txt[end] in count_track:
             count_track[txt[end]]+=1 
            else:
                count_track[txt[end]]=1
            
            if count_track[txt[start-1]]==1:
                count_track.pop(txt[start-1])
            else:
                count_track[txt[start-1]]-=1
            if original_count==count_track:
                answer+=1
            end+=1 
            start+=1 
        return answer
