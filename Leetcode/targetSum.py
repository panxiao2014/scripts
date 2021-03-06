#You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
#Find out how many ways to assign symbols to make sum of integers equal to target S.
#
#Example 1:
#Input: nums is [1, 1, 1, 1, 1], S is 3. 
#Output: 5
#Explanation: 
#
#-1+1+1+1+1 = 3
#+1-1+1+1+1 = 3
#+1+1-1+1+1 = 3
#+1+1+1-1+1 = 3
#+1+1+1+1-1 = 3
#
#There are 5 ways to assign symbols to make the sum of nums be target 3.
#
#Tips: use a stack to implement DFS tree. Each nod is a full path from root to current node, so we can know its sum, also all the node along this path

class Solution:
    def printOutput(self, node):
      s = ""
      for i in range(1, len(node)):
        num = node[i]
        if(num >= 0):
          s += ("+" + str(num))
        else:
          s += str(num)
      s += "="
      s += str(S)
      print(s) 

    def findTargetSumWays(self, nums, S):
      numLevel = len(nums)
      
      #a node is represented as a list of the path to the node, for example: [0, 1, 1, -1]:
      rootNode = [0]
      
      ret = 0
      
      numStack = [rootNode]
      while(len(numStack) != 0):
        curNode = (numStack.pop())
        curLevel = len(curNode) - 2
        
        nextLevel = curLevel + 1
        nextNum = nums[nextLevel]
        
        if(nextLevel == (numLevel-1)):
        #reaching the last num, so check the sum:
          if((sum(curNode)+nextNum) == S):
            ret += 1

            retList = curNode.copy()
            retList.append(nextNum)
            self.printOutput(retList)

            #if the list contains 0, then need extra attention, since +0 and -0 are the same result:
            zeros = curNode.count(0)
            if(zeros > 1):
              ret += 2**(zeros-1)-1
          elif((sum(curNode)-nextNum) == S):
            ret += 1
            
            retList = curNode.copy()
            retList.append(nextNum*(-1))
            self.printOutput(retList)

            zeros = curNode.count(0)
            if(zeros > 1):
              ret += 2**(zeros-1)-1
        else:
          nextNode1 = curNode.copy()
          nextNode1.append(nextNum)
          
          numStack.append(nextNode1)
          
          if(nextNum == 0):
            continue
          else:          
            nextNode2 = curNode.copy()
            nextNode2.append(nextNum*(-1))
        
            numStack.append(nextNode2)

          
      return ret

import sys


#nums = [35,16,11,38,44,5,17,20,23,0,27,46,38,29,22,18,27,34,12,10] 
#S = 22

nums = [40,2,49,50,46,6,5,23,38,45,45,17,4,26,40,33,14,9,37,24]
S = 7

#nums = [1,1,1,1,1]
#S = 3

#nums = [5,8,2,3,9,7,10,6]
#S = 2

solution = Solution()
ret = solution.findTargetSumWays(nums, S)

print("There are %d ways" % ret)

