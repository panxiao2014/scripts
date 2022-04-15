#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
#Note that an empty string is also considered valid.


class Solution:
    def isValid(self, s: str):
        def isPair(s1, s2):
          if(s1 == '(' and s2 == ')'):
            return True
          if(s1 == '[' and s2 == ']'):
            return True
          if(s1 == '{' and s2 == '}'):
            return True
          return False
        
        self.stack = []
        self.strLen = len(s)
        self.cursor = -1
        
        if(self.strLen == 0):
          return True
        elif(self.strLen == 1):
          return False
        
        for i in range(0, self.strLen):
          if(self.cursor == -1):
            self.stack.append(s[i])
            self.cursor += 1
            continue
          if(isPair(self.stack[self.cursor], s[i]) == False):
            self.stack.append(s[i])
            self.cursor += 1
          else:
            self.stack.pop()
            self.cursor -= 1
            
        if(len(self.stack) == 0):
          return True
        else:
          return False

import sys

s = sys.argv[1]

solution = Solution()
print(solution.isValid(s))
