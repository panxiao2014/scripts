#Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
#Example 1:
#Input: n = 12
#Output: 3 
#Explanation: 12 = 4 + 4 + 4.
#
#Example 2:
#Input: n = 13
#Output: 2
#Explanation: 13 = 4 + 9.

import sys

target = int(sys.argv[1])

class Node:
  def __init__(self, nextN=None, prevN=None, number=None, currentSum=None, isRoot=False):
    self.nextN=nextN
    self.prevN=prevN
    self.number=number
    self.currentSum=currentSum
    self.isRoot=isRoot

  #print the numbers that added to the target:
  def printRoute(self):
    routeList = []
    node = self
    while(node.isRoot == False):
      routeList.append(node)
      node = node.prevN

    routeList.append(node)
    routeStr = ""
    for i in routeList:
      if i.isRoot == True:
        routeStr = routeStr + str(i.number)
      else:
        routeStr = routeStr + str(i.number) + "+"
    print(routeStr)

class Solution:
  def numSquares(self, n):
    if (n==1):
      return 1

    squareBase = 1
    squareNum = squareBase**2

    #this list contains all square numbers less than target number:
    squareList = []
    while(squareNum < n):
      squareList.append(squareNum)
      squareBase += 1
      squareNum = squareBase**2
      if(squareNum == n):
        return 1

    import queue
    q = queue.Queue()
    for squareNum in squareList:
      node = Node(None, None, squareNum, squareNum, True)
      q.put(node)

    steps = 0
    while(1):
      steps += 1
      for i in range(0, q.qsize()):
        node = q.get()

        currentSum = node.currentSum

        if(steps > 1 and (currentSum in squareList)):
          continue

        squareNum = node.number

        #for each node, the next step to add a square number, it only add square numbers which are equal or greater than itself:
        squareL = list(filter(lambda x: x>=squareNum, squareList))
        for number in squareL:
          newTotalSum = number+currentSum
          if(newTotalSum > n):
            break

          newNode = Node(None, node, number, newTotalSum, False)
          node.nextN = newNode
          
          if(newTotalSum == n):
            newNode.printRoute()
            return steps +1

          q.put(newNode)


    return 0




solution = Solution()
numbers = solution.numSquares(target)
print(numbers)
