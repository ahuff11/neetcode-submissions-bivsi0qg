class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for s in range(len(words)):
            for c in range(len(words[s])):
                if c >= len(words) or s >= len(words[c]) or words[s][c] != words[c][s]:
                    return False

        return True