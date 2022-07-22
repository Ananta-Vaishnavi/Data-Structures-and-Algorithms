from collections import Counter
txt = 'aabaabaa'
pat = 'aaba'
def search(pat, txt):
    answer=0
    original_count=dict(Counter(pat))
    count_track={}
    for i in range(len(pat)):
        if txt[i] in count_track:
            count_track[txt[i]]+=1 
        else:
            count_track[txt[i]]=1
    start=0
    end=len(pat)-1
    while end!=len(txt):
        if txt[end] in count_track:
            count_track[txt[end]]+=1 
        else:
            count_track[txt[end]]=1
        if start>0 and count_track[txt[start-1]]==1:
            count_track.pop(txt[start-1])
        else:
            count_track[txt[start-1]]-=1
        if original_count==count_track:
            answer+=1
        end+=1 
        start+=1 
    return answer
print(search(pat,txt))
