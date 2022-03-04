class Solution:
    def isValid(self, s):
        """
        type s: str
        rtype: bool
        """
        stack = []
        for x in s:
            if x == '(' or x == '[' or x == "{": 
                stack.append(x)
            else:
                if len(stack) == 0 or (stack[-1] == "(" and x != ")") or (stack[-1] == "{" and x != "}") or (stack[-1] == "[" and x != "]"): 
                    return False
                stack.pop()
        return len(stack) == 0