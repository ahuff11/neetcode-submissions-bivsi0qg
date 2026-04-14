class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #two pointer sliding window. 
        myset = set()
        longest = 0
        l,r = 0, 0
        while r != len(s):
            if s[r] not in myset:
                myset.add(s[r])
                longest = max(longest, r-l+1)
                r+=1

            else:
                myset.remove(s[l])
                l+=1
 
        return longest
