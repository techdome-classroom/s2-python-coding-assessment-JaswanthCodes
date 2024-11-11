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
        
        # Iterate through each character in the input string
        for char in s:
            # If it's a closing bracket, check if it matches the top of the stack
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, else use a dummy value '#'
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the corresponding opening bracket, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets were matched correctly
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))        # Output: True
print(solution.isValid("()[]{}"))    # Output: True
print(solution.isValid("(]"))        # Output: False
print(solution.isValid("([)]"))      # Output: False
print(solution.isValid("{[]}"))      # Output: True







    



  

