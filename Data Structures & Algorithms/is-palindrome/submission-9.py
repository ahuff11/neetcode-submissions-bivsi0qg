class Solution:
    def isPalindrome(self, s: str) -> bool:
        #turn string into no spaces and lowercase and ignore special characters
        #two pointer iterate and check if equal to each other
        s = "".join(c for c in s if c.isalnum()).lower()
        l , r = 0, len(s)-1
        print(s)
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l+=1
                r-=1
        return True
