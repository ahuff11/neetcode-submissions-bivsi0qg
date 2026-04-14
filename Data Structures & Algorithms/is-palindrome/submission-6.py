class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''.join(filter(str.isalnum, s.lower()))
        print(s2)
        i = 0
        j = len(s2)-1
        while i != len(s2)//2:
            print(i, s2[i], j, s2[j])
            if s2[i] != s2[j]:
                return False
            i+=1
            j-=1
     
        return True