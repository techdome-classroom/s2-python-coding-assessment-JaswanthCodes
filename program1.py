class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))        # Output: True
print(solution.isValid("()[]{}"))    # Output: True
print(solution.isValid("(]"))        # Output: False
print(solution.isValid("([)]"))      # Output: False
print(solution.isValid("{[]}"))      #

