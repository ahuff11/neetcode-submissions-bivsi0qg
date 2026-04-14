class Solution:


    #get the len of string and append a number and # in front of it to tell how many integers to count to decode it

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += str(len(s))+'#'+s
        return ans



    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i+length
            ans.append(s[i:j])
            i = j

        return ans