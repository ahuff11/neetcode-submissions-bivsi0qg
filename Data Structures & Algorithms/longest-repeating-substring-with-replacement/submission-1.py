class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #SLIDING WINDOW and keep a hash map for frequency of characters
        l = r = 0
        hashy = {}
        replacements = 0
        count_of_most_frequent = 0
        max_freq = 0
        for r in range(len(s)):
            hashy[s[r]] = 1 + hashy.get(s[r], 0)
            count_of_most_frequent = max(hashy[s[r]], count_of_most_frequent)
            replacements = (r-l+1) - count_of_most_frequent
            while replacements > k:
                hashy[s[l]] -=1
                l+=1
                replacements = (r-l+1) - count_of_most_frequent
                
            
            max_freq = max(replacements+ count_of_most_frequent, max_freq)
        return max_freq