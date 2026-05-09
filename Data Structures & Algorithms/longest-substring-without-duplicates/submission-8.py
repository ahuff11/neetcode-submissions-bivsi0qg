class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicates = set()
        L, length = 0, 0

        for R in range(len(s)):
            while s[R] in duplicates:
                duplicates.remove(s[L])
                L+=1
            duplicates.add(s[R])
            length = max(R-L+1, length)

        return length