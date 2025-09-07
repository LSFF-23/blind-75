class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [s[0]]
        for i in range(1, len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
                continue
            if len(stack) == 0: 
                return False
            li = len(stack) - 1
            if (s[i] == ")" and stack[li] != "(") or (s[i] == "]" and stack[li] != "[") or (s[i] == "}" and stack[li] != "{"):
                return False
            stack.pop()
        return len(stack) == 0

s = Solution()
assert s.isValid("()") == True, "#1"
assert s.isValid("()[]{}") == True, "#2"
assert s.isValid("(]") == False, "#3"
assert s.isValid("([])") == True, "#4"
assert s.isValid("([)]") == False, "#5"
assert s.isValid("]") == False, "#6"
assert s.isValid("(){}}{") == False, "#7"