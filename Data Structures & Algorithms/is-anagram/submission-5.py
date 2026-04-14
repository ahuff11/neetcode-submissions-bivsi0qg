class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tt = {}
        ss = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in ss:
                ss[s[i]] +=1
            else:
                ss[s[i]] =1
            if t[i] in tt:
                tt[t[i]] +=1
            else:
                tt[t[i]] = 1

        print(ss)
        print(tt)
        return ss == tt