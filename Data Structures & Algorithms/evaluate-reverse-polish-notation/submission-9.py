class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for c in tokens:
            if c in {"+", "-", "*", "/"}:
                if c == '+':
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(a+b)
                elif c == '-':
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(a-b)
                elif c == '/':
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(int(a/b))
                elif c == '*':
                    b = nums.pop()
                    a = nums.pop()
                    nums.append(a*b)
            else:
                nums.append(int(c))
        return nums.pop()