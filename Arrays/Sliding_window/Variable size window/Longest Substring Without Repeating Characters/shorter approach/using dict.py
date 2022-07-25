def lengthOfLongestSubstring(s):
#         Approach 2
        occur = {}
        l =0
        output = 0
        for r in range(len(s)):
            if s[r] not in occur:
                output = max(output,r-l+1)
            else:
                if occur[s[r]]<l:
                    output = max(output,r-l+1)
                else:
                    l = occur[s[r]]+1
            occur[s[r]] = r
        return output
print(lengthOfLongestSubstring('abcabcaa'))
