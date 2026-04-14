from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashy = defaultdict(list)
        ans = []
        for word in strs:
            sword = "".join(sorted(word))
            if sword in hashy:
                hashy[sword].append(word)
            else:
                hashy[sword].append(word)
        for value in hashy.values():
            ans.append(value)

        return ans