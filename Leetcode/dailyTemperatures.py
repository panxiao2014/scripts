#Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.
#
#For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
#
#Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

class Solution:
    def dailyTemperatures(self, T):
      days = len(T)
      if(days <= 1):
        return [0]
      
      ret = []
      for i in range(0, days):
        ret.append(0)
        
      dayStack = []
      dayStack.append([T[0], 0])
      stackCursor = 0
      
      for i in range(1, days):
        temper = T[i]
        while(stackCursor >= 0 and temper > dayStack[stackCursor][0]):
          ret[dayStack[stackCursor][1]] = i - dayStack[stackCursor][1]
          dayStack.pop()
          stackCursor -= 1
          
        dayStack.append([temper, i])
        stackCursor += 1
          
      return ret

import sys

tempers = [73, 74, 75, 71, 69, 72, 76, 73]
solution = Solution()
print(solution.dailyTemperatures(tempers))
